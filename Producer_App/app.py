from flask import Flask, jsonify
from controller.blueprint import controller

app = Flask(__name__)

app.register_blueprint(controller)

if __name__ == '__main__':
    app.run(debug=True)