from flask import jsonify, request

from flaskr import api, db
from flask_restful import Resource
from flaskr.entities.Client import Client


class ClientListAPI(Resource):
    def get(self):
        clients = Client.query.all()
        return jsonify([client.serialize() for client in clients])


class RegisterAPI(Resource):
    def post(self):
        json_data = request.get_json(force=True)

        if 'username' not in json_data:
            return {"message": "The client provided can't be registered! A client requires a username"}
        if 'host' not in json_data:
            return {"message": "The client provided can't be registered! A client requires a host"}

        client = Client(
            username=json_data['username'],
            host=json_data['host']
        )
        db.session.add(client)
        db.session.commit()

        return {"message": f"Created a new client with username {client.username}"}, 201


api.add_resource(ClientListAPI, '/clients')
api.add_resource(RegisterAPI, '/register')
