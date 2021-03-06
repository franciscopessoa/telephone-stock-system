from app import db
from flask import request
from ..models.user import User, UserSchema
from flask_sieve import Sieve, Validator
from sqlalchemy.exc import SQLAlchemyError
from app.utils import formatResponse
import jwt
from datetime import datetime, timedelta
import config
from functools import wraps
from app.utils import formatResponse

def login():    
    rules = {
        'username': ['required', 'bail'],
        'password': ['required', 'bail']
    }
    messages = {
        'username.required': 'É necessário informar o seu login',
        'password.required': 'É necessário informar a senha de acesso',
    }
    validator = Validator(rules=rules, messages=messages, request=request)

    if validator.passes():
        try:
            body = request.get_json(force=True)
            user = User.query.filter_by(username=body['username']).first()
            if user is None:
                return formatResponse("", "Usuário ou senha inválidos", 400)

            if user.check_password(body['password']):
                user_schema = UserSchema()
                result = user_schema.dump(user)

                token = jwt.encode({
                            'user_id': result['id'],
                            'exp': datetime.utcnow() + timedelta(hours=24)
                        }, config.SECRET_KEY)
                return formatResponse({"token" : token}, "Login efetuado com sucesso")
            return formatResponse("", "Usuário ou senha inválidos", 400)
        except SQLAlchemyError as e:
            return formatResponse("", str(e.__dict__['orig']), 500, True)
    return formatResponse(validator.messages(), "validation_errors", 400)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        jwtToken = None
        if 'Authorization' in request.headers:
            jwtToken = request.headers['Authorization']
        if not jwtToken or not jwtToken.startswith("Bearer "):
            return formatResponse("", "Unauthorized Access!", 401)

        try:
            bearer, token = jwtToken.split(" ");
            data = jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
        except jwt.InvalidTokenError as e:
            return formatResponse("", "Unauthorized Access!", 401)
        return f(*args, **kwargs)
    return decorated
