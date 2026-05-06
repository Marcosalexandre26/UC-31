from flask import Flask, render_template

app = Flask(_name_)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    nome = "Marcosss"
    return render_template('index.html', title='Página inicial', nome=nome)

@app.route('/dados', defaults={"nome": "usuário comum"})
@app.route('/dados/<nome>')
def dados(nome):
    return f'Olá, {nome}!'

@app.route('/semestre/<int:x>')
def semestre(x):
    return 'Estamos no semestre ' + str(x)

@app.route('/pagamento/<float:valor>')
def pagamento(valor):
    return 'Você pagou: ' + str(valor)


@app.route('/arearestrita/<int:id>')
def arearestrita(id):
    if id == 1:
        cadeado = 'fechado'
    elif id == 2:
        cadeado = 'aberto'
    else:
        cadeado = None

    return render_template('arearestrita.html', cadeado=cadeado)


@app.route('/operacao/<tipo>/<float:op1>/<float:op2>')
def operacao(tipo, op1, op2):
    if tipo == 'sum':
        resultado = op1 + op2
    elif tipo == 'sub':
        resultado = op1 - op2
    elif tipo == 'mult':
        resultado = op1 * op2
    elif tipo == 'div':
        resultado = op1 / op2
    else:
        return 'Tipo inválido. Use: sum, sub, mult ou div'

    return render_template('operacao.html', resultado=resultado)

if _name_ == '_main_':
    app.run(debug=True)