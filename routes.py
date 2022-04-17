

@app.route('/')
def index():
    all_data = Data.query.all()
    return render_template('index.html', malha=all_data)


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


@app.route('/update', methods=['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))

        my_data.rota = request.form['rota']
        my_data.corte = request.form['corte']
        my_data.freq = request.form['freq']
        my_data.origem = request.form['origem']
        my_data.destino = request.form['destino']

        db.session.commit()
        flash("Rota atualizada com sucesso!")

        return redirect(url_for('index'))


@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Rota deletada com sucesso!")

    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Acesso solicitado por {form.username.data}, lembrar-me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)