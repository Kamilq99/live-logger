from flask import Blueprint, request, jsonify
from model.logs import Logs

controller = Blueprint('controller', __name__)

@controller.route('/logs', methods=['POST'])
def send_logs():
    data = request.get_json()
    name = data['name']
    message = data['message']

    log = Logs(name, message)
    return jsonify(log.send_log())