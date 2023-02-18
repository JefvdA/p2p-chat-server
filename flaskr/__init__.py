from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db = SQLAlchemy()
db.init_app(app)

from flaskr.entities.Client import Client

with app.app_context():
    db.create_all()

api = Api(app)

from flaskr import views
