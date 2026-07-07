from App import app
from flask import render_template, request, jsonify
from database import db
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/', methods=['GET', 'POST'])
def pesquisar():

    valorPesquisa = ""

    if request.method == 'POST':
        valorPesquisa = request.form["pesquisa"]
        print(valorPesquisa)

    return render_template(
        "index.html",
        valorPesquisa=valorPesquisa
    )
#-----------cad user ----------------
@app.route('/cadastro', methods=['POST'])
def cadUser():
    try:
        banco = db()
        cursor = banco.cursor()

        dados = request.get_json() or {}

        valoremail = dados.get('email')
        valornome = dados.get('nome')
        valorsenha = dados.get('senha')

       

        if not valoremail or not valornome or not valorsenha:
            return jsonify({'menssage': ' erro, todos os campos sao obrigatorios'})
        
        senha_hash = generate_password_hash(valorsenha)
        
        sql = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)"
        cursor.execute(sql, (valornome, valoremail, senha_hash))

    except Exception as erro:
        jsonify({'algo deu errado' : str(erro)})

    banco.commit()
    banco.close()

    return "Usuário cadastrado!"


