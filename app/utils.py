from flask import jsonify
import os

def formatResponse(data, message = "", statusCode = 200, internalError = False):
    if internalError and os.environ.get("FLASK_ENV") == "production":
        message = "Oops, ocorreu um erro interno no servidor, por favor comunique a equipe de desenvolvimento"
    return jsonify({"message": message, "data" : data}), statusCode