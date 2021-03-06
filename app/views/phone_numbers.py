from app import db
from flask import request, jsonify
from ..models.phone_number import PhoneNumber, PhoneNumberSchema
from flask_sieve import Sieve, Validator
from sqlalchemy.exc import SQLAlchemyError
from app.utils import formatResponse
import math    

def show(id):
    try:
        number = PhoneNumber.query.filter_by(id=id).first()
        number_schema = PhoneNumberSchema()
        result = number_schema.dump(number)
        return formatResponse(result)
    except SQLAlchemyError as e:
        return formatResponse("", str(e.__dict__['orig']), 500, True)

def index():
    try:
        body = request.args.to_dict()
        page       = int(body['page'])
        firstLimit = int(body['limit'])
        limit      = firstLimit if firstLimit < 100 else 100
    except:
        return formatResponse("", "pagina e limite são requeridos, limite máximo: 100", 400, True)

    try:
        get_numbers = PhoneNumber.query.limit(limit).offset((page - 1) * limit).all()
        numbers_schema = PhoneNumberSchema(many=True)
        numbers = dict(
            paginate = numbers_schema.dump(get_numbers),
            total = PhoneNumber.query.count()
            ) 
        return formatResponse(numbers)
    except SQLAlchemyError as e:
        return formatResponse("", str(e.__dict__['orig']), 500, True)

def delete(id):    
    try:
        row = PhoneNumber.query.filter_by(id=id).first()
        if (row is None):
            return formatResponse("", "Não foi encontrado nenhum registro a ser deletado", 400)

        db.session.delete(row)
        db.session.commit()
        return formatResponse("", "Número removido com sucesso")
    except SQLAlchemyError as e:
        return formatResponse("", str(e.__dict__['orig']), 500, True)

def store():    
    rules = {
        'value': ['required','max:25', 'bail'],
        'monthy_price': ['required', 'bail'],
        'setup_price': ['required', 'bail'],
        'currency': ['required','max:3', 'bail'],
    }
    messages = {
        'value.required': 'É necessário informar um número de telefone',
        'value.max': 'O tamanho máximo para o número de telefone é 25',
        'monthy_price.required': 'É necessário informar o preço mensal',
        'setup_price.required': 'É necessário informar o preço de configuração',
        'currency.required': 'É necessário informar o tipo de moeda',
        'currency.max': 'É tamanho máximo para o tipo de moeda é 3',
    }
    validator = Validator(rules=rules, messages=messages, request=request)

    if validator.passes():
        body = request.get_json(force=True)

        if float(body['monthy_price']) < 0:
            return formatResponse("", "O valor mensal não pode ser negativo", 400)
        if float(body['setup_price']) < 0:
            return formatResponse("", "O valor de configuração não pode ser negativo", 400)

        row = PhoneNumber.query.filter_by(value=body['value']).first()
        if row:
            return formatResponse("", "Este número já está cadastrado", 400)

        phone_numbers = PhoneNumber(**body)

        try:
            db.session.add(phone_numbers)
            db.session.commit()
            numbers_schema = PhoneNumberSchema()
            result = numbers_schema.dump(phone_numbers)
            return formatResponse(result, "Número inserido com sucesso")
        except SQLAlchemyError as e:
            return formatResponse("", str(e.__dict__['orig']), 500, True)
    return formatResponse(validator.messages(), "validation_errors", 400)

def update(id):    
    rules = {
        'value': ['required','max:25', 'bail'],
        'monthy_price': ['required', 'bail'],
        'setup_price': ['required', 'bail'],
        'currency': ['required','max:3', 'bail'],
    }
    messages = {
        'value.required': 'É necessário informar um número de telefone',
        'value.max': 'O tamanho máximo para o número de telefone é 25',
        'monthy_price.required': 'É necessário informar o preço mensal',
        'setup_price.required': 'É necessário informar o preço de configuração',
        'currency.required': 'É necessário informar o tipo de moeda',
        'currency.max': 'É tamanho máximo para o tipo de moeda é 3',
    }
    validator = Validator(rules=rules, messages=messages, request=request)

    if validator.passes():
        body = request.get_json(force=True)

        if float(body['monthy_price']) < 0:
            return formatResponse("", "O valor mensal não pode ser negativo", 400)
        if float(body['setup_price']) < 0:
            return formatResponse("", "O valor de configuração não pode ser negativo", 400)

        try:
            numbers_schema = PhoneNumberSchema()

            # validation with number exists
            row            = PhoneNumber.query.filter_by(value=body['value']).first()
            data           = numbers_schema.dump(row)
            if row and data['id'] != id:
                return formatResponse("", "Este número já está cadastrado", 400)

            # validation with number not exists
            number  = PhoneNumber.query.filter_by(id=id).first()
            if (number is None):
                return formatResponse("", "Número não cadastrado", 400)

            dataNumber = PhoneNumber(**body)
            
            number.value        = dataNumber.value
            number.monthy_price = dataNumber.monthy_price
            number.setup_price  = dataNumber.setup_price
            number.currency     = dataNumber.currency
            db.session.commit()
            numbers_schema = PhoneNumberSchema()
            result         = numbers_schema.dump(dataNumber)
            result['id']   = id 
            return formatResponse(result, "Número atualizado com sucesso")
        except SQLAlchemyError as e:
            return formatResponse("", str(e.__dict__['orig']), 500, True)
    return formatResponse(validator.messages(), "validation_errors", 400)
