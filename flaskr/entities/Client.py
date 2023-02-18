from flaskr import db
import bcrypt


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    host = db.Column(db.String, nullable=False)

    def __init__(self, username, password, host):
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt(12))
        self.host = host

    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'username': self.username,
            'host': self.host
        }
