from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Funcionario(db.Model):
    __tablename__ = 'funcionario'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)