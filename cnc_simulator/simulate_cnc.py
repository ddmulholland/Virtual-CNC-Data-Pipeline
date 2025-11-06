# simulate_cnc.py
"""
Program to simulate CNC data for usage with other programs.
CNC machine generates a random spindle speed [1000-3000], random temperature [25-75], random status
"""

import random
import time
import requests
import json

MACHINE_ID = 'CNC_01'
# TODO: Add machine specific settings (chipoad, N of flutes, set rpm, feedrate)
API_URL = 'http://127.0.0.1:5000/update'

SPEED_MIN, SPEED_MAX = 1000, 3000
TEMP_MIN, TEMP_MAX = 25.0, 75.0

def generate_data():
  """
  Simulate cnc machine data telemetry packet.
  Scalable to multiple items.
  Uses spindle speed, temperature, and current status.
  """
  return {
      "machine_id": MACHINE_ID,
      "spindle_speed": random.randint(SPEED_MIN, SPEED_MAX),
      "temperature": random.uniform(
          TEMP_MIN, TEMP_MAX
      ),  # TODO: add probability to each random occurance, in future flag out of range values, specifically overheating
      "status": random.choice(['RUNNING', 'IDLE', 'FAULT']),
  }


def main():
  while True:
    data = generate_data()
    print(f"Sending: {data}")
    # try:
    #   requests.post(API_URL, json=data)
    # except Exception as e:
    #   print(f"Error sending data: {e}")
    time.sleep(2)


if __name__ == "__main__":
  main()
