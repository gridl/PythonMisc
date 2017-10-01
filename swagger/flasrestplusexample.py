from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/wth')
class Test(Resource):
    def get(self):
        return {"what the": 'hell'}

if __name__ == '__main__':
    app.run(debug=True,port=8001)