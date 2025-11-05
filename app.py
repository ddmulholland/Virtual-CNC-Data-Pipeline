from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import random
import time
from datetime import datetime

app = Flask(__name__, static_folder='static')
CORS(app)

class CNCMachineSimulator:
    def __init__(self):
        self.machine_id = "CNC-001"
        self.status = "running"
        self.temperature = 45.0
        self.spindle_speed = 3000
        self.feed_rate = 500
        self.position = {"x": 0.0, "y": 0.0, "z": 0.0}
        
    def simulate_step(self):
        self.temperature += random.uniform(-0.5, 1.0)
        self.temperature = max(40, min(80, self.temperature))
        
        self.spindle_speed += random.randint(-100, 100)
        self.spindle_speed = max(2000, min(5000, self.spindle_speed))
        
        self.feed_rate += random.randint(-50, 50)
        self.feed_rate = max(200, min(1000, self.feed_rate))
        
        self.position["x"] += random.uniform(-0.5, 0.5)
        self.position["y"] += random.uniform(-0.5, 0.5)
        self.position["z"] += random.uniform(-0.1, 0.1)
        
        for axis in ["x", "y", "z"]:
            self.position[axis] = max(-100, min(100, self.position[axis]))
    
    def get_data(self):
        self.simulate_step()
        return {
            "machine_id": self.machine_id,
            "timestamp": datetime.now().isoformat(),
            "status": self.status,
            "temperature": round(self.temperature, 2),
            "spindle_speed": self.spindle_speed,
            "feed_rate": self.feed_rate,
            "position": {
                "x": round(self.position["x"], 3),
                "y": round(self.position["y"], 3),
                "z": round(self.position["z"], 3)
            },
            "vibration": round(random.uniform(0.1, 2.5), 2),
            "power_consumption": round(random.uniform(3.5, 8.5), 2)
        }

simulator = CNCMachineSimulator()

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/api/data')
def get_data():
    data = simulator.get_data()
    return jsonify(data)

@app.route('/api/status')
def get_status():
    return jsonify({
        "machine_id": simulator.machine_id,
        "status": simulator.status,
        "uptime": "running"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
