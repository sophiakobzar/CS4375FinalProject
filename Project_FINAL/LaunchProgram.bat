@echo off
echo Starting server...
start cmd /k "cd /d %~dp0 & python server.py"
timeout /T 5 /nobreak
start http://127.0.0.1:5000/