#!/bin/sh
echo Starting server...
python server.py &
delay 5
open http://localhost:5000/
