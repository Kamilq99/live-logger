from flask import Blueprint, request, jsonify
from kafka import KafkaProducer
from model.logs import Logs

controller = Blueprint('controller', __name__)

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@controller.route('/logs', methods=['POST'])
def send_logs():
    data = request.get_json()
    if not data or 'name' not in data or 'message' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    producer.send('logs', data)
    producer.flush()
    
    return jsonify(log.send_log())