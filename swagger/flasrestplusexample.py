from flask import Flask, request
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/wth')
class Test(Resource):
    def get(self):
        return {"what the": 'hell'}

todos = {}

@api.route('/<string:todo_id>')
class ToDoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}





if __name__ == '__main__':
    app.run(debug=True,port=8001)