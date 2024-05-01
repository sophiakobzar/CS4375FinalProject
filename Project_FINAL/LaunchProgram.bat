@echo off
echo Starting server...
start cmd /k "cd /d %~dp0 & python server.py"
timeout /T 5 /nobreak
start http://localhost:5000/