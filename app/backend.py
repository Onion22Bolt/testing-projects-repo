from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/')
def get_instance_info():
    instance_id = socket.gethostname()
    public_ip = socket.gethostbyname(instance_id)
    return jsonify(instanceId=instance_id, publicIp=public_ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)