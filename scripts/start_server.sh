#!/bin/bash
cd app

# Stop if already running
pkill -f "flask" || true

# Start Flask API
nohup python3 api.py > output.log 2>&1 &
