from flask import Flask

app = Flask(__name__)

@app.route('/ola/<nome>')
def saudacao(nome):
    return f'Olá, {nome}! Seja muito bem vindo(a) ao sistema!!!!!!!!!!!!!!!!!.'

@app.route('/calculo/<int:n1>/<int:n2>')
def calculo(n1, n2):
    return f'A soma de {n1} + {n2} da {n1 + n2}'

@app.route('/idade/<nome>/<int:idade>')
def verificar_idade(nome, idade):
    if idade >= 18:
        return f'{nome} ja e maior de idade.'
    return f'{nome}e menor de idade.'

@app.route('/produto/<nome>/<float:preco>')
def produto(nome, preco):
    return f'O produto {nome} custa $ {preco:.2f}'

@app.route('/repetir/<palavra>/<int:vezes>')
def repetir(palavra, vezes):
    return ' '.join([palavra] * vezes)

if __name__ == '__main__':
    app.run(debug=True)