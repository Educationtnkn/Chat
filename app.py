from flask import Flask, jsonify, request
import json

app = Flask(__name__)
FILE_PATH = 'chat.json'

@app.route('/read', methods=['GET'])
def read_data():
    with open(FILE_PATH, 'r') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/write', methods=['POST'])
def write_data():
    request_data = request.get_json()
    with open(FILE_PATH, 'w') as file:
        json.dump(request_data, file, indent=2)
    return jsonify({'message': 'Data written successfully'})

if __name__ == '__main__':
    app.run(debug=True)
