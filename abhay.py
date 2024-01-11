from flask import Flask ,request , jsonify
import json 
import os

app=Flask(__name__)

data='data.json'

@app.route('/tasks',methods=['POST'])
def create_task():
    new_task = request.get_json()

    
    if os.path.exists(data):
        with open(data, 'w') as file:
            json.dump([], file)

    with open(data, 'r') as file:
        tasks = json.load(file)

    new_task['id'] = len(tasks) + 1  
    tasks.append(new_task)

    with open(data, 'w') as file:
        json.dump(tasks, file, indent=2)

    return jsonify(new_task)
    


# Read kern h
@app.route('/tasks', methods=['GET'])
def get_tasks():
    
    if os.path.exists(data):
        with open(data, 'r') as file:
            tasks = json.load(file)
        return jsonify(tasks)
    else:
             return jsonify([])


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    if os.path.exists(data):
        with open(data, 'r') as file:
            tasks = json.load(file)
            task = next((t for t in tasks if t['id'] == task_id), None)
            if task:
                return jsonify(task)
            else:
                return jsonify({"error": "Task not found"}), 404
    else:
        return jsonify({"error": "No tasks available"}), 404
    
if __name__ =="__main__":
    app.run(debug=True)