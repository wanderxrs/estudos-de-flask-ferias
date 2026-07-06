from flask import Flask

app = Flask(__name__)

from App.routs import login, contatos
