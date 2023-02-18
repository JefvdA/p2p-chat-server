from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db = SQLAlchemy()
migrate = Migrate(app, db)
db.init_app(app)

from flaskr.entities.Client import Client

with app.app_context():
    db.create_all()

api = Api(app)

from flaskr import views
