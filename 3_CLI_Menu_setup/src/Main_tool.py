# Backend app (Flask or another)

from flask import Flask, request, jsonify

print("Starting backend...")
app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

