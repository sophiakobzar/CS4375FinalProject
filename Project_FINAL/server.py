from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import subprocess
import shlex
import threading
import queue
import sys

app = Flask(__name__)
socketio = SocketIO(app)
input_queue = queue.Queue()
script_thread = None

def run_script():
    global input_queue
    script_path = "spamDetection.py"
    python_executable = sys.executable
    process = subprocess.Popen([python_executable, script_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)
    while True:
        line = process.stdout.readline()
        print(f"Script says: {line}")
        if not line:
            break
        socketio.emit('script_output', {'data': line})
        if ("5: Exit" in line or 
            "Do you want to test your own email (Yes or No)?" in line or 
            "Example input (without quotes): 'Subject: I am skydiving'" in line):
            choice = input_queue.get()
            print(f"Sending input to script: {choice}")
            process.stdin.write(f"{choice}\n")
            process.stdin.flush()
    stdout, stderr = process.communicate()
    socketio.emit('script_output', {'data': stdout + stderr})

@app.route('/')
def GUI():
    return render_template('GUI.html')

@socketio.on('start_script')
def handle_start_script():
    global script_thread
    if script_thread is None or not script_thread.is_alive():
        script_thread = threading.Thread(target=run_script)
        script_thread.start()
        return "Script started"
    return "Script is already running"

@socketio.on('send_input')
def handle_input(message):
    print(f"Received input: {message['data']}")
    input_queue.put(message['data'])

@socketio.on('disconnect')
def handle_disconnect():
    global script_thread
    if script_thread.is_alive():
        print("Starting script thread...")
        script_thread.terminate()  
        script_thread.join()
    else:
        print('Script is already running')
    print("Client disconnected")

if __name__ == '__main__':
    socketio.run(app, debug=True)