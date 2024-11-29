from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from main import Main
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'App is running'

@app.route('/chat', methods=["GET","POST"])
def chat():
    data = request.data.decode("utf-8")
    res = Main(data)
    return jsonify({'res' : res})

if __name__ == '__main__':
    app.run(debug=True)
