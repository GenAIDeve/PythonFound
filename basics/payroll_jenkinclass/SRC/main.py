# flask app for payroll endpoint
from flask import Flask, request, jsonify
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    return app

def create_app():
    app = Flask(__name__)
    CORS(app)
    return app
