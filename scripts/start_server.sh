#!/bin/bash
cd /home/ec2-user/ml-app/app
pkill -f "flask"
nohup python3 api.py > output.log 2>&1 &
