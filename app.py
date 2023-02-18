from flaskr import app, db

if __name__ == '__main__':
    app.run()
    db.init_app(app)
    db.create_all()
