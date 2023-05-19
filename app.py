from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'  
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        user_data = {'id': user.id, 'name': user.name, 'email': user.email}
        result.append(user_data)
    return jsonify(result)

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({'message': 'User not found'})
    user_data = {'id': user.id, 'name': user.name, 'email': user.email}
    return jsonify(user_data)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(data['name'], data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'})

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({'message': 'User not found'})
    data = request.get_json()
    user.name = data['name']
    user.email = data['email']
    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({'message': 'User not found'})
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    db.create_all()
    app.run()
