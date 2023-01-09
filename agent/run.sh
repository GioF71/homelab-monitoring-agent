#!/usr/bin/env bash

# Show env vars
grep -v '^#' .env

# Export env vars
export $(grep -v '^#' .env | xargs)

export DB_CREDENTIALS_FILE="db-credentials.txt"

echo "DB_CREDENTIALS_FILE=[$DB_CREDENTIALS_FILE]"

python3 homelab_monitoring_agent/monitor.py
