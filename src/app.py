from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

todos =[ 
  { 
    "label": "My first task", 
     "done": False 
     } ]


@app.route('/todos', methods=['GET'])
def hello_world():
  json_text = jsonify(todos)
  return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
  request_body = request.json
  todos.append(request_body)
  return jsonify(todos), 200
  #print("Incoming request with the following body", request_body)
  #return 'Response for the POST todo'


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
  del todos[position]
  return jsonify(todos), 200




# These two lines shoul
# d always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)