#!/bin/usr/python3.5
from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
import os
import sys

app = Flask(__name__)
api = Api(app)
ipadd = "23.123.34.123"

#ttest = {
#    'telnet': {'ipadd': os.system('telnet ' + str(ipadd))},
#    'ping': {'ipadd':  os.system('./ping.sh '+ str(ipadd) + ' ping')},
#    'ping': {'ipadd':  os.system('python ' + pingresutl.py + " " + str(ipadd) + ' ping')},
#    'ping': {'ipadd':  os.system('ping ' + ipadd + ' -c ' + '2')},
#    'traceroute': {'ipadd': os.system('traceroute ' + str(ipadd))},
#    'mtr': {'ipadd': os.system('mtr ' + str(ipadd))}
#}

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
#	1: "telnet",
#	2: "ping",
#	3: "traceroute",
#	4: "mtr"
#}

def readfle(file_name):
    f=open(file_name, "r")
    if f.mode == 'r':
	contents = f.read()
	t_result = [contents]
    return t_result	

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return ttest[todo_id]

#    def post(self, todo_id):
#        args = parser.parse_args()
#        todo_id = int(max(ttest.keys()).lstrip('todo')) + 1
#        todo_id = 'todo%i' % todo_id
#        ttest[todo_id] = {'task': args['task']}
#	return jsonify({'ip': str(ipadd),'Command': ttest[todo_id],'result': args['task']}), 201
#	return ttest[todo_id], 201

    def put(self, todo_id):
        args = parser.parse_args()
	file_name = todo_id + args
	f= open(file_name,"w+")
	result = os.system(todo_id + ' ' + args + ' -c 2 >> ' + file_name)
	test_result = readfle(file_name)
	task = {'task': test_result}
        ttest[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return ttest

#    def post(self):
#        args = parser.parse_args()
#        todo_id = int(max(ttest.keys()).lstrip('todo')) + 1
#        todo_id = 'todo%i' % todo_id
#        ttest[todo_id] = {'task': args['task']}
#	return {'ip': str(ipadd),'Command': ttest[todo_id],'result': args['task']}, 201
#	return ttest[todo_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
