#!/bin/bash
# Start Jupyter in the background
jupyter lab --ip=0.0.0.0 --port=8888 --allow-root --no-browser &

# Wait a few seconds for server to start
sleep 5

# Extract the token
TOKEN=$(jupyter server list | grep -oP '(?<=token=)[a-z0-9]+')

# Print token in a copy-friendly format
echo "************************"
echo "************************"
echo "token: $TOKEN"
echo "************************"
echo "************************"

# Keep Jupyter running
wait
