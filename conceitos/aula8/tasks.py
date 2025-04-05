from flask import Flask, request, jsonify, render_template
import sqlite3
from pathlib import Path

root = Path(__file__).parent.resolve()
db = root / "tasks.db"

app = Flask(__name__)

# Define a simple auth token
AUTH_TOKEN = "a3f5c8e1d4b6a7c9e2f3b4d5c6a7e8f"

# Middleware to check the token
def require_auth(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if token != f"Bearer {AUTH_TOKEN}":
            return jsonify({"message": "Unauthorized"}), 401
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__  # Preserve the original function name
    return wrapper

@app.route('/')
def index():
    conn, cursor = openConnection()
    createTable(cursor)
    closeConnection(conn)
    return render_template('tasks.html')

@app.route('/tasks', methods=["GET"])
@require_auth
def getTasks():
    conn, cursor = openConnection()
    cursor.execute("SELECT * FROM tasks")
    tasks = [{"id": row[0], "name": row[1]} for row in cursor.fetchall()]
    closeConnection(conn)
    if not tasks:
        return jsonify({"message": "Task list is empty"}), 200
    return jsonify(tasks), 200

@app.route('/tasks/<taskName>', methods=["POST"])
@require_auth
def addTask(taskName):
    conn, cursor = openConnection()
    cursor.execute("INSERT INTO tasks (name) VALUES (?)", (taskName,))
    conn.commit()
    task_id = cursor.lastrowid
    closeConnection(conn)
    return jsonify({"id": task_id, "name": taskName}), 201

@app.route('/tasks/<int:id>', methods=["DELETE"])
@require_auth
def removeTask(id):
    conn, cursor = openConnection()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    closeConnection(conn)
    if cursor.rowcount == 0:
        return jsonify({"message": "Task not found"}), 404
    return jsonify({"message": "Task deleted"}), 200

@app.route('/tasks/<int:id>/<taskName>', methods=["PUT"])
@require_auth
def updateTask(id, taskName):
    conn, cursor = openConnection()
    cursor.execute("UPDATE tasks SET name = ? WHERE id = ?", (taskName, id))
    conn.commit()
    closeConnection(conn)
    if cursor.rowcount == 0:
        return jsonify({"message": "Task not found"}), 404
    return jsonify({"message": "Task updated", "id": id, "name": taskName}), 200

def openConnection():
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error as e:
        print("Cannot connect to database", e)
        return None, None

def closeConnection(conn):
    if conn:
        conn.close()

def createTable(cursor):
    try:
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        ''')
    except sqlite3.Error as e:
        print("Error creating table:", e)

if __name__ == '__main__':
    app.run(debug=True)