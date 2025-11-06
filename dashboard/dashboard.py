import streamlit as st 
import pandas as pd
import sqlite3


st.set_page_config(page_title="Connected Factory Dashboard", layout="wide")

def load_data():
  with sqlite3.connect("../collector/factory_data.db") as conn:
    df = pd.read_sql_query("SELECT * FROM cnc_data ORDER BY id DESC LIMIT 100", conn) # get most recent 1000 entries
  return df

st.title("Connected Factory Dashboard")
st.markdown("Real-time CNC telemetry visualization")

data = load_data()

if not data.empty:
  st.metric("Latest Machine", data.iloc[0]["machine_id"])
  st.metric("Spindle Speed", f"{data.iloc[0]["spindle_speed"]} RPM")
  st.metric("Temperature", f"{data.iloc[0]["temperature"]} deg C")
else:
  st.warning("No data available.")