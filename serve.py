from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def post():
    # Start the stress_cpu.py script in a non-blocking manner
    subprocess.Popen(['python', 'stress_cpu.py'])
    return 'CPU stress script started', 202

@app.route('/', methods=['GET'])
def get():
    # Return the private IP address of the EC2 instance
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)
    return private_ip

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)