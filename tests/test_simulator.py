# test_simulator.py
"""
Procedural tests for simulate_cnc.py
Validate behavior and data integrity of the sim.
"""

import pytest
import json
from unittest.mock import patch
from cnc_simulator import simulate_cnc

def test_generate_data_structure():
  """Make sure generate_data() returns the correct values + types"""
  data = simulate_cnc.generate_data()
  expected_keys = {
    "machine_id", 
    "spindle_speed", 
    "temperature", 
    "status"}
  assert set(data.keys()) == expected_keys, "Incorrect keys in data package"

  # check types
  assert isinstance(data["machine_id"], str)
  assert isinstance(data["spindle_speed"], int)
  assert isinstance(data["temperature"], float)
  assert isinstance(data["status"], str)

# make sure value ranges are correct
def test_generate_data_values():
  for _ in range(50):
    data = simulate_cnc.generate_data()
    assert simulate_cnc.SPEED_MIN <= data["spindle_speed"] <= simulate_cnc.SPEED_MAX
    assert simulate_cnc.TEMP_MIN <= data["temperature"] <= simulate_cnc.TEMP_MAX
    assert data["status"] in {"RUNNING", "IDLE", "FAULT"}

