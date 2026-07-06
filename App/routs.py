from App import app
from flask import render_template, url_for

@app.route('/')
def login():

    usuario = 'Nyedson' 
    idade = 20
    
    dados = {
        'usuario' : 'ny',
        'idade' : 22
    }
    return render_template ('index.html', usuario = usuario, idade = idade, dados = dados)

@app.route('/contatos')
def contatos():
    return render_template ('novo.html')
