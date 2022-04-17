from main import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rota = db.Column(db.String(20))
    corte = db.Column(db.String(20))
    freq = db.Column(db.String(30))
    origem = db.Column(db.String(50))
    destino = db.Column(db.String(50))

    def __init__(self, rota, corte, freq, origem, destino):
        self.rota = rota
        self.corte = corte
        self.freq = freq
        self.origem = origem
        self.destino = destino


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self) -> str:
        return f'<Usuario {self.username}>'


