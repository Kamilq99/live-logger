from flask import Flask, request, jsonify
import json

bp = Blueprint("producer", __name__)

@bp.route("/")
def index():
    return "Flask App run check sending data to Kafka", 200

@bp.route("/send", methods=["POST"])
def send_messege():
    try:
        data = request.get_json()
        topic = data.get("topic", "default_topic")
        messege = data.get("message", {})

        sent_to_kafka(topic, messege)
        reutrn jsonify({"status": "sent", "topic": topic}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500