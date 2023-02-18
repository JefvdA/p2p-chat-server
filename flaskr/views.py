from flask import jsonify, request

from flaskr import api, db
from flask_restful import Resource
from flaskr.entities.Client import Client


class ClientListAPI(Resource):
    def get(self):
        clients = Client.query.all()
        return jsonify([client.serialize() for client in clients])


class ClientAPI(Resource):
    def get(self, username):
        client = Client.query.filter_by(username=username).first()
        return jsonify(client.serialize())

    def delete(self, username):
        client = Client.query.filter_by(username=username).first()
        json_data = request.get_json(force=True)

        if 'password' not in json_data:
            return {"message": f"The client with username {username} can't be deleted! A password should be provided"}
        password = json_data['password']

        if not client.check_password(password):
            return {"message": f"The client with username {username} can't be deleted! The password provided was wrong"}

        db.session.delete(client)
        db.session.commit()
        return {"message": f"The client with username {username} was deleted!"}


class RegisterAPI(Resource):
    def post(self):
        json_data = request.get_json(force=True)

        if 'username' not in json_data:
            return {"message": "The client provided can't be registered! A client requires a username"}
        if 'password' not in json_data:
            return {"message": "The client provided can't be registered! A client requires a password"}
        if 'host' not in json_data:
            return {"message": "The client provided can't be registered! A client requires a host"}

        client = Client(
            username=json_data['username'],
            password=json_data['password'],
            host=json_data['host']
        )
        db.session.add(client)
        db.session.commit()

        return {"message": f"Created a new client with username {client.username}"}, 201


api.add_resource(ClientListAPI, '/clients')
api.add_resource(ClientAPI, '/clients/<username>')
api.add_resource(RegisterAPI, '/register')
