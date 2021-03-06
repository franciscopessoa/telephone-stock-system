from app import app
from app.views import users
from app.views import phone_numbers
from app.views import auth

# Users routes
@app.route('/users', methods=['POST'])
def store_user():
    return users.store()

# Auth routes
@app.route('/login', methods=['POST'])
def login():
    return auth.login()

# Numbers routes
@app.route('/number/<int:id>', methods=['GET'])
def show(id):
    return phone_numbers.show(id)

@app.route('/numbers', methods=['GET'])
def index():
    return phone_numbers.index()

@app.route('/number/<int:id>', methods=['DELETE'])
def delete_number(id):
    return phone_numbers.delete(id)

@app.route('/numbers', methods=['POST'])
def store_number():
    return phone_numbers.store()

@app.route('/number/<int:id>', methods=['PUT'])
def update_number(id):
    return phone_numbers.update(id)

# Invalid route
@app.route('/<path:path>')
def catch_all(path):
    return {"message" : "invalid route", "data": ""}