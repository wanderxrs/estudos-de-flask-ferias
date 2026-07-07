from App import app
from flask import render_template, request, jsonify
from database import db

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
        valoremail = dados['email']
        valornome = dados['nome']
        valorsenha = dados['senha']

        if not valoremail or not valornome or not valorsenha:
            return jsonify({'menssage': ' erro ao cadastrar, veriique se suas informações sao válidas'})
        
        sql = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)"
        cursor.execute(sql, (valornome, valoremail, valorsenha, ))

    except:
        return 'algo deu errado'

    banco.commit()
    banco.close()

    return "Usuário cadastrado!"


