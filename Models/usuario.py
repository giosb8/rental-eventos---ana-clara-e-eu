from flask_sqlalchemy import flask_SQLAlchemy

db = flask_SQLAlchemy()

class Usuario(db.Model):
    __tablename__= 'usuario'

    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(100), nullable=False) 
    email = db.Column(db.String(100), unique=True, nullable=False)
