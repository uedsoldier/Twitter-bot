#!/bin/bash

# Set PATH explicitly for cron
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Load environment variables
set -a
source /app/.env
set +a

# Change to script directory
cd /app/src || exit 1

# Log start with timestamp
echo "[$(date)] Starting bot execution..."

# Run the Python script with full path
/usr/local/bin/python main.py

# Log completion
echo "[$(date)] Bot execution completed"
