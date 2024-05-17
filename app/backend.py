from flask import Flask, jsonify, send_from_directory, url_for
import socket

app = Flask(__name__, static_folder='static')

@app.route('/')
def homepage():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api')
def get_instance_info():
    instance_id = socket.gethostname()
    public_ip = socket.gethostbyname(instance_id)
    return jsonify(instanceId=instance_id, publicIp=public_ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
