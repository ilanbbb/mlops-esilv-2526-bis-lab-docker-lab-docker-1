import os
import platform
import sys
from flask import Flask, send_from_directory
from flask_cors import CORS
from datetime import datetime

if 'CURRENT_ENVIRONMENT' not in os.environ:
    print('===================================================================', file=sys.stderr)
    print('[ERROR] Missing value for CURRENT_ENVIRONMENT envrionment variable.', file=sys.stderr)
    print('[ERROR] Please specify it when you start the container.', file=sys.stderr)
    sys.exit(1)

# Create logs folder
os.makedirs(name="./logs", exist_ok=True)

app = Flask(__name__, static_folder='../front')
CORS(app)

@app.route('/front')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/')
def default():
    return {
        "time": str(datetime.now()),
        "environment": os.environ['CURRENT_ENVIRONMENT'],
        "hostname": platform.uname()[1],
        "result": "root"
    }    

@app.route("/get/<name>")
def get(name):
    return {
        "time": str(datetime.now()),
        "environment": os.environ['CURRENT_ENVIRONMENT'],
        "hostname": platform.uname()[1],
        "result": name
    }

@app.route("/write/<something>")
def write(something):
    print(something)
    with open('logs/my-messages.log', 'a') as the_file: 
        the_file.write(f"{something}\n")
    return {
        "status": "ok"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)