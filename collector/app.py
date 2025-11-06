from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

DB_PATH = "factory_data.db"

def init_db():
  with sqlite3.connect(DB_PATH) as conn:
    conn.execute("""
    CREATE TABLE IF NOT EXISTS cnc_data (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      machine_id TEXT,
      spindle_speed INTEGER,
      temperature REAL,
      status TEXT,
      timestamp DATETIME
    );
    """)

@app.route("/update", methods=["POST"])
def update_data():
  data = request.get_json()
  if not data:
    return jsonify({"error": "No data"}), 400
  with sqlite3.connect(DB_PATH) as conn:
    conn.execute(
      """INSERT INTO cnc_data (
      machine_id,
      spindle_speed,
      temperature,
      status,
      timestamp
      )
      VALUES
      (?, ?, ?, ?, ?)
      """,
      (data["machine_id"],
      data["spindle_speed"],
      data["temperature"],
      data["status"],
      datetime.now())
    )
  return jsonify({"message": "Data logged successfully"}), 200


if __name__ == "__main__":
  init_db()
  app.run(debug=True)
  