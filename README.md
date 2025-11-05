# Virtual-CNC-Data-Pipeline
Simulation of Flow for CNC Machine Data &amp; Visualization


Goal: Simulate the flow of CNC machine telemetry data &rarr; store in SQL &rarr; visualize KPIs 

Why: Demonstrate ability to emulate shop floor connectivity and data analytics

Key Skills: Ptyhon, SQL, MQTT (simulate), dashboards

- Use python to generate simulated CNC Data; temperature, spindle speed, tool wear, status.
- Stream data via MQTT or a RESTful API endpoint into PostgreSQL database.
- Build simple Flask dashboard to represent:
  - machine uptime
  - alarm rates
  - avg spindle util
  - tool-change frequency trends