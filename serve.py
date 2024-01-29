from flask import Flask, request, jsonify
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def handle_request():
    if request.method == 'POST':
        subprocess.Popen(['python', 'stress_cpu.py'])
        return jsonify({'message': 'Stressing CPU initiated'})

    elif request.method == 'GET':
        private_ip = socket.gethostbyname(socket.gethostname())
        return jsonify({'private_ip': private_ip})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
