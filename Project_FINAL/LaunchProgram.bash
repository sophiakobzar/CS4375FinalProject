#!/bin/bash
echo Starting server...
python server.py &
sleep 5
sensible-browser http://localhost:5000/