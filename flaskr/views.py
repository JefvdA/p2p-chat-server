from flaskr import api
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('client')


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class Register(Resource):
    def post(self):
        args = parser.parse_args()
        client = args['client']

        if 'username' not in client:
            return {"message": "The client provided can't be registered! A client requires a username"}
        if 'host' not in client:
            return {"message": "The client provided can't be registered! A client requires a host"}

        print(client)

        return {"message": "ok"}, 201


api.add_resource(HelloWorld, '/')
api.add_resource(Register, '/register')
