from flaskr import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    host = db.Column(db.String, nullable=False)

    def __init__(self, username, host):
        self.username = username
        self.host = host

    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'username': self.username,
            'host': self.host
        }
