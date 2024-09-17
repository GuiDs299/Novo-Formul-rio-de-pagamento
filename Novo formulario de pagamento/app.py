from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def formulario():
    return render_template('formulario.html')


@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    metodo_pagamento = request.form['metodo_pagamento']

    if metodo_pagamento == 'cartao':
        numero_cartao = request.form['numero_cartao']
        validade = request.form['validade']
        cvv = request.form['cvv']
        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")
        print(f"Número do Cartão: {numero_cartao}")
        print(f"Validade: {validade}")
        print(f"CVV: {cvv}")
    elif metodo_pagamento == 'pix':
        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")
        print("Pagamento via Pix")

    return redirect(url_for('formulario'))


if __name__ == '__main__':
    app.run(debug=True)
