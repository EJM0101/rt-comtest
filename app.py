from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rtcomtestsecret'
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("start_simulation")
def handle_simulation(data):
    method = data.get("method")

    if method == "pipe":
        socketio.emit("log_update", "Pipe: Tâche A écrit: [Message 1]")
        socketio.emit("bubble", "Message 1")
        time.sleep(1)
        socketio.emit("log_update", "Tâche B lit: [Message 1]")

    elif method == "semaphore":
        socketio.emit("log_update", "🔒 Tâche A prend la ressource")
        socketio.emit("bubble", "🔒")
        time.sleep(2)
        socketio.emit("log_update", "⏳ Tâche B en attente...")
        time.sleep(2)
        socketio.emit("log_update", "✅ Tâche A libère → Tâche B accède")

    elif method == "queue":
        for i in range(1, 4):
            socketio.emit("log_update", f"Tâche A → file: [Msg {i}]")
            socketio.emit("bubble", f"Msg {i}")
            time.sleep(0.5)
        for i in range(1, 4):
            socketio.emit("log_update", f"Tâche B lit: [Msg {i}]")
            time.sleep(1)

    elif method == "socket":
        socketio.emit("log_update", "Tâche A: Hello B 👋")
        socketio.emit("bubble", "👋")
        time.sleep(1)
        socketio.emit("log_update", "Tâche B: Hello A ✅")
        socketio.emit("bubble", "✅")
        time.sleep(1)

    socketio.emit("log_update", "🎯 Simulation terminée.")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host="0.0.0.0", port=port)