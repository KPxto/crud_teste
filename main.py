from cProfile import run
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import psycopg2


app = Flask(__name__)
app.secret_key = "Senha"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kaio:25123436@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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

        



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/insert', methods=['POST'])
def insert():

    if request.method == 'POST':
        rota = request.form['rota']
        corte = request.form['corte']
        freq = request.form['freq']
        origem = request.form['origem']
        destino = request.form['destino']

        my_data = Data(rota, corte, freq, origem, destino)
        db.session.add(my_data)
        db.session.commit()

        flash("Rota criada com sucesso!")

        return redirect(url_for('index'))





if __name__ == '__main__':
    app.run(debug=True)
