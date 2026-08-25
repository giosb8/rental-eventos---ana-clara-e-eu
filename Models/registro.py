class Registro(db.Model):
    _tablename__ Registro
    id = db.Column(db.Integer,primary_key=True)
    cliente_resp = db.Column(db.String(100), nullable=False) 
    data_movimentacao = db.Column(db.Datetime, nullable=False)
    tipo_movimentacao = db.Column(db.String(100))
    quantidade = db.Column(db.Integer)

    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionario.id'))
    equipamento_id = db.Column(db.Integer, db.ForeignKey('equipamento.id'))
