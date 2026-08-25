class Equipamento(db.Model):
    __tablename__ = 'equipamento'

    id = db.Column(db.Integer,primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    potencial = db.Column(db.String(100), nullable=False)
    material = db.Column(db.String(100), nullable=False)
    peso = db.Column(db.Float, nullable=False)
    dimensoes = db.Column(db.Numeric(10, 2))
    cor = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
	