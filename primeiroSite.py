from flask import Flask

app = Flask(__name__)
#route -> saolourencodaserradoacoes.com/contatos
#função -> o que você quer exibir naquela página

@app.route("/")
def homepage():
    return

@app.route("/")
def contatos():
    return "Nossos contatos são: E-mail: trabalhounivesp@gmail.com Telefone(11)99999-9999"

@app.route("/")
def usuários():
    return
#colocar o site no ar

if __name__=="__main__":
    app.run(debug=True)