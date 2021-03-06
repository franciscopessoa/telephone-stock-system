from app import db
from flask import request
from ..models.user import User, UserSchema
from flask_sieve import Sieve, Validator
from sqlalchemy.exc import SQLAlchemyError
from app.utils import formatResponse

def store():    
    rules = {
        'username': ['required','max:50', 'bail'],
        'password': ['required', 'min:8', 'bail'],
        'name': ['required', 'max:200', 'bail'],
        'email': ['required','email', 'max:120', 'bail'],
    }
    messages = {
        'username.required': 'É necessário informar o username',
        'username.max': 'O tamanho máximo para o username é: 50',
        'password.required': 'É necessário informar uma senha válida',
        'password.min': 'Sua senha deve ter no mínimo 8 caracteres',
        'name.required': 'É necessário informar o campo nome',
        'name.max': 'O tamanho máximo para o campo nome é: 200',
        'email.required': 'É necessário informar o campo email',
        'email.email': 'O email informado é inválido',
        'email.max': 'O tamanho máximo para o campo email é:120',
    }
    validator = Validator(rules=rules, messages=messages, request=request)

    if validator.passes():
        body = request.get_json(force=True)

        try:
            usernameExists = User.query.filter_by(username=body['username']).first()
            if usernameExists:
                return formatResponse("", "Este username já está sendo utilizado", 400)

            emailExists = User.query.filter_by(email=body['email']).first()
            if emailExists:
                return formatResponse("", "Este email já está sendo utilizado", 400)

            user = User(**body)
            user.hash_password()
            db.session.add(user)
            db.session.commit()
            user_schema = UserSchema()
            result = user_schema.dump(user)
            del result['password']
            return formatResponse(result, "Usuário cadastrado com sucesso")
        except SQLAlchemyError as e:
            return formatResponse("", str(e.__dict__['orig']), 500, True)
    return formatResponse(validator.messages(), "validation_errors", 400)
