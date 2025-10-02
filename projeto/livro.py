from projeto import db

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    descricao = db.Column(db.String(100))
    valor = db.Column(db.Integer)
    
    def __init__(self, name, descricao, valor):
      self.name = name 
      self.descricao = descricao
      self.valor = valor