from flask import Flask, request, jsonify

app = Flask(__name__)
id = 0
tasksList = []

@app.route('/tasks', methods=["GET"])
@app.route('/tasks/', methods=["GET"])
def getTasks():
  global tasksList
  if not tasksList :
    return "Task list is empty", 200
  else :
    return jsonify(tasksList), 200

@app.route('/tasks/<taskName>', methods=["POST"])
def addTask(taskName):
  global id
  id = id + 1
  task = {"id": id, "name": taskName}
  tasksList.append(task)
  return jsonify(task), 201

@app.route('/tasks/<int:id>', methods=["DELETE"])
def removeTask(id) :
  global tasksList
  for i, task in enumerate(tasksList):
      if task["id"] == id:
          deleted_task = tasksList.pop(i)
          return jsonify({"message": "Task deleted", "task": deleted_task}), 200
  return jsonify({"message": "Task not found"}), 404

@app.route('/tasks/<int:id>/<taskName>', methods=["PUT"])
def updateTask(id, taskName) :
  global tasksList
  for i, task in enumerate(tasksList) :
    if task["id"] == id :
      updated_task = tasksList[i]
      tasksList[i]["name"] = taskName
      return jsonify({"message": "Task Updated", "task": updated_task}), 200
  return jsonify({"message": "Task not found"}), 404
  

if __name__ == '__main__':
  app.run(debug=True)