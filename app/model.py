from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure(app):
    db.init_app(app) #agroup configure like a link
    app.db = db # help to call in a route

# Creating a table and conecting to database
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    livro = db.Column(db.String(255))
    escritor = db.Column(db.String(255))