from flask import Flask, request, jsonify

app = Flask(__name__)

users={}
next_user_id = 1

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users),200

@app.route('/users', methods=['POST'])
def create_user():
    global next_user_id
    data = request.get_json()

    if not data or 'name' not in data or 'email' not in data:
        return jsonify({'error': 'name and email are required'}),400
    
    user_id = next_user_id
    users[user_id] = {
        'name': data['name']
        }
    next_user_id += 1
    return jsonify({'id': user_id, **users[user_id]}),201

@app.route('/users/<int:user_id>', methods = ["PUT"])
def update_user(user_id):
    data = request.json
    user = users.get(user_id)
    if not user:
        return jsonify({'error':'user not found'}),404
    
    user['name']= data.get('name', user['name'])
    user['email']= data.get('email', user['email'])
    return jsonify(user),200

@app.route('/users/<int:user_id>', methods =['DELETE'])
def delete_user(user_id):
    if user_id in users:
     deleted_user= users.pop(user_id)
     return jsonify({'message': 'user deleted', 'user':deleted_user}),200
    else:
     return jsonify({'error': 'user not found'}),404

if __name__=='__main__':
    app.run(debug=True)