from flask import jsonify

from flaskr import api, db
from flask_restful import Resource, reqparse
from flaskr.entities.Client import Client

parser = reqparse.RequestParser()
parser.add_argument('client')


class ClientList(Resource):
    def get(self):
        clients = db.session.execute(db.select(Client).order_by(Client.username))
        return jsonify({'clients': [dict[client] for client in clients]})


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


api.add_resource(ClientList, '/')
api.add_resource(Register, '/register')
