#!/bin/usr/python3.5
from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
import os
import sys
import subprocess

app = Flask(__name__)
api = Api(app)
#ipadd = "23.123.34.123"

# ttest = {
#    'telnet': {'ipadd': os.system('telnet ' + str(ipadd))},
#    'ping': {'ipadd':  os.system('ping ' + ipadd + ' -c ' + '2')},
#    'traceroute': {'ipadd': os.system('traceroute ' + str(ipadd))},
#    'mtr': {'ipadd': os.system('mtr ' + str(ipadd))}
# }

ttest = {
    'telnet': {'ipadd': 'telnet ipadd'},
    'ping': {'ipadd': 'ping ipadd'},
    'traceroute': {'ipadd': 'traceroute ipadd'},
    'mtr': {'ipadd': 'mtr ipadd'}
}

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in ttest:
        abort(404, message="Network Troubleshooting Test {} doesn't exist".format(todo_id))

#def switch_test(args):
#    switcher = {
#       1: "telnet",
#       2: "ping",
#       3: "traceroute",
#       4: "mtr"
#}

def result(todo_id, ipadd):
    if todo_id == 'ping':
       c_result = subprocess.run(['ping', ipadd, '-c 2'], stdout=subprocess.PIPE)
    elif todo_id == 'mtr':
       c_result = subprocess.run(['mtr -c 1 -r', str(ipadd), '-o "LSRD NBWA JXIM V"'], stdout=subprocess.PIPE)
    elif todo_id == 'traceroute':
       c_result = subprocess.run(['traceroute -n ', str(ipadd)], stdout=subprocess.PIPE)
    else:
        c_result = subprocess.run(['telnet -d ', str(ipadd)], stdout=subprocess.PIPE)
    return c_result

# def readfle(file_name):
#     f=open(file_name, "r")
#     if f.mode == 'r':
#         contents = f.read()
#         t_result = [contents]
#     return t_result

# parser = reqparse.RequestParser()
# parser.add_argument('task')
parser = reqparse.RequestParser()
parser.add_argument('ipadd', required=True, help="IP Address cannot be blank!")


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return ttest[todo_id]

    def post(self, todo_id):
        ipadd = parser.parse_args()
#        todo_id = int(max(ttask.keys()).lstrip('ipadd')) + 1
#        todo_id = 'todo%i' % todo_id
        command_result = result(todo_id, ipadd)
        return jsonify({'ip': str(ipadd), todo_id : command_result}), 201

    def put(self, todo_id):
        ipadd = parser.parse_args()
        todo_id = int(max(ttask.keys()).lstrip('ipadd')) + 1
        todo_id = 'todo%i' % todo_id
        command_result = result(todo_id, ipadd)
        return jsonify({'ip': str(ipadd), todo_id : command_result}), 201

# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return ttest


##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)

