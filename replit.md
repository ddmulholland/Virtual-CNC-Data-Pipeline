# Virtual CNC Data Pipeline

## Overview
This project simulates a CNC (Computer Numerical Control) machine data pipeline with real-time visualization. It provides a web-based dashboard that displays simulated machine metrics including temperature, spindle speed, feed rate, position, vibration, and power consumption.

## Purpose
- Demonstrate real-time data flow from a simulated CNC machine
- Visualize machine metrics through an interactive web dashboard
- Provide a foundation for building industrial IoT monitoring applications

## Current State
- Fully functional web application with Flask backend and vanilla JavaScript frontend
- Real-time data simulation with 1-second update intervals
- Responsive dashboard with gradient charts and live metric displays

## Recent Changes
- **2025-11-05**: Initial project setup
  - Created Flask API backend with CNC machine simulator
  - Implemented frontend dashboard with real-time data visualization
  - Configured for Replit environment with port 5000
  - Added workflow configuration for automatic server startup

## Project Architecture

### Backend (`app.py`)
- **Framework**: Flask 3.0.0 with CORS support
- **Simulator**: `CNCMachineSimulator` class generates realistic machine data
- **API Endpoints**:
  - `GET /`: Serves the main dashboard
  - `GET /api/data`: Returns current machine metrics
  - `GET /api/status`: Returns machine status information
- **Host Configuration**: Binds to 0.0.0.0:5000 for Replit compatibility

### Frontend (`static/`)
- **index.html**: Main dashboard layout with metric cards
- **style.css**: Responsive design with gradient backgrounds and card-based UI
- **app.js**: Real-time data fetching and chart rendering using Canvas API

### Data Simulation
The simulator tracks and updates:
- Temperature (40-80°C range)
- Spindle Speed (2000-5000 RPM)
- Feed Rate (200-1000 mm/min)
- 3-axis Position (X, Y, Z within ±100mm)
- Vibration (0.1-2.5 mm/s)
- Power Consumption (3.5-8.5 kW)

## Dependencies
- Python 3.11
- Flask 3.0.0
- Flask-CORS 4.0.0

## Usage
The application starts automatically via the configured workflow. Access the dashboard through the Replit webview to see real-time CNC machine metrics updating every second.

## Future Enhancement Ideas
- Add historical data logging and trend analysis
- Implement alerts for abnormal readings
- Add multiple machine support
- Include data export functionality
- Add authentication for production use
