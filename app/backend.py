from flask import Flask, request, jsonify
from prometheus_client import start_http_server, Summary, Counter, generate_latest, REGISTRY
import requests
import time
import threading

app = Flask(__name__)

# Prometheus metrics
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
CPU_USAGE = Counter('cpu_usage', 'CPU usage')

# Root endpoint
@app.route('/')
def index():
    return "Hello, World!"

# Prometheus metrics endpoint
@app.route('/metrics')
def metrics():
    return generate_latest(REGISTRY)

# TheHive alert endpoint
@app.route('/alert')
def alert():
    data = {
        "title": "DDoS Alert",
        "description": "Potential DDoS attack detected.",
        "source": "Prometheus",
        "type": "alert"
    }
    headers = {
        'Authorization': 'Bearer UH91C/Y9cLq0DlX0cIb1f0Kaeul//3hQ',  # TheHive API key
        'Content-Type': 'application/json'
    }
    response = requests.post('http://192.168.70.173:9000/api/alert', json=data, headers=headers)  
    if response.status_code == 201:
        return jsonify({"message": "Alert sent successfully"})
    else:
        return jsonify({"message": "Failed to send alert", "details": response.json()}), response.status_code

# Trigger DDoS simulation
@app.route('/trigger-ddos')
def trigger_ddos():
    def ddos_attack():
        start_time = time.time()
        while time.time() - start_time < 10:  # Simulate a DDoS attack for 10 seconds
            requests.get('http://localhost:5000/')
            CPU_USAGE.inc()  # Simulate CPU usage increment
    thread = threading.Thread(target=ddos_attack)
    thread.start()
    return "DDoS simulation triggered"

if __name__ == '__main__':
    start_http_server(8000)  # Prometheus metrics server
    app.run(host='0.0.0.0', port=5000)


# from flask import Flask, jsonify, send_from_directory, url_for
# import socket

# app = Flask(__name__, static_folder='static')

# @app.route('/')
# def homepage():
#     return send_from_directory(app.static_folder, 'index.html')

# @app.route('/api')
# def get_instance_info():
#     instance_id = socket.gethostname()
#     public_ip = socket.gethostbyname(instance_id)
#     return jsonify(instanceId=instance_id, publicIp=public_ip)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8080)
