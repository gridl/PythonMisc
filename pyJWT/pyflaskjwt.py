from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required,current_identity

app = Flask(__name__)

app.config['SECRET_KEY'] = 'super-secret'
api = Api(app,prefix='/api/v1')

# class PrivateResource(Resource):
#     def get(self):
#         return {"meaning of life": 42}


#api.add_resource(PrivateResource, '/private')

USER_DATA = {
    "vish":"abc123"

}

# construct the jwt instance


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

def identity(payload):
    user_id = payload['identity']
    return {"user_id":user_id}
# the identity function will recieve the decoded JWT

jwt = JWT(app, verify, identity)

class PrivateResource(Resource):
    @jwt_required()
    def get(self):
        #return {"meaning of life": 42}
        return dict(current_identity)

api.add_resource(PrivateResource,'/private')
if __name__ == '__main__':
    app.run(debug=True, port=5000)

    # we pass the flask app instance, authentication function and identity function to the JWT class

    # http://127.0.0.1:5000/api/v1/private


# to get an auth token, send a POST request to /auth with a JSON payload with username and password

# curl -H "Content-Type: application/json" -X POST -d '{"username":"vish","password":"abc123"}' http://localhost:5000/auth

# curl -X GET http://localhost:5000/api/v1/private -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTIzNTM1NTksImlhdCI6MTUxMjM1MzI1OSwiaWRlbnRpdHkiOjEyMywibmJmIjoxNTEyMzUzMjU5fQ.hYibp1qr1kb0HxKSqIzrZBK8P2VgwD3h38AbyZJgERA"

# curl -X GET http://localhost:5000/api/v1/private -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYmYiOjE1MTIzNTM2MzAsImlkZW50aXR5IjoxMjMsImlhdCI6MTUxMjM1MzYzMCwiZXhwIjoxNTEyMzUzOTMwfQ.DOjF6E3cMRFiZI2hBACX2uYTjXURREhJ3qYA8lsEnBQ"