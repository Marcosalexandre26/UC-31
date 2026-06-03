from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/cadastro', methods=['POST'])
def cadastro():

    nome = request.form.get('nome', '').strip().title()
    email = request.form.get('email', '').strip().lower()
    telefone = request.form.get('telefone', '').strip()
    cpf = request.form.get('cpf', '').strip()
    cidade = request.form.get('cidade', '').strip().title()
    estado = request.form.get('estado', '').strip().upper()
    curso = request.form.get('curso', '')
    idade = request.form.get('idade', '').strip()
    senha = request.form.get('senha', '').strip()

    telefone = telefone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    cpf = cpf.replace(".", "").replace("-", "")

    if len(nome) < 8:
        return "Nome inválido"

    if "@" not in email or ".com" not in email:
        return "E-mail inválido"

    if len(telefone) != 11:
        return "Telefone inválido"

    if len(cpf) != 11:
        return "CPF inválido"

    if len(cidade) < 3:
        return "Cidade inválida"

    if len(estado) != 2:
        return "Estado inválido"

    if curso == "":
        return "Escolha um curso"

    if not idade.isdigit():
        return "Idade inválida"

    if int(idade) < 16:
        return "Idade mínima é 16 anos"

    if len(senha) < 8:
        return "Senha muito fraca"

    return f"""
    <h1 style="color:green;">Cadastro concluído com sucesso!</h1>

    <p><b>Nome:</b> {nome}</p>
    <p><b>E-mail:</b> {email}</p>
    <p><b>Telefone:</b> {telefone}</p>
    <p><b>CPF:</b> {cpf}</p>
    <p><b>Cidade:</b> {cidade}</p>
    <p><b>Estado:</b> {estado}</p>
    <p><b>Curso:</b> {curso}</p>
    <p><b>Idade:</b> {idade}</p>

    <br>
    <a href="/">Voltar</a>
    """


if __name__ == '__main__':
    app.run(debug=False)