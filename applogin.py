from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://localhost:27017')
db = client['language']

@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.json

        if 'username' not in data or 'password' not in data:
            return jsonify({'message': 'Missing required fields'}), 400

        username = data['username']
        password = data['password']

        db.translator.insert_one({
    'username': username,
    'password': password
}, w=1)

        return jsonify({'message': 'Data stored successfully'}), 200
    except Exception as e:
        print('Error:', e)
        return jsonify({'message': 'Data failed to store in the backend.'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')