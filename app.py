
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Realty Bot API"

@app.route('/api/private')
def private():
    return jsonify({'message': 'Private API access granted.'})
