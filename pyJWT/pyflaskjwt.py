from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app,prefix='/api/v1')

class PrivateResource(Resource):
    def get(self):
        return {"meaning of life": 42}


api.add_resource(PrivateResource, '/private')

USER_DATA = {
    "vish":"abc123"

}

class User(object):
    def __init__(self,id):
        self.id = id

    def __str__(self):
        return "User(id='%s')" % self.id

def verify(username, password):
    if not (username and password):
        return False
    if USER_DATA.get(username) == password:
        return User(id=123)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
    # http://127.0.0.1:5000/api/v1/private



