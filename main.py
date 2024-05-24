from flask import Flask, render_template, request, redirect
app = Flask(__name__)

#Lista
contatos = []

@app.route('/')
def index():
    return render_template('index.html', contatos=contatos)

@app.route('/adicionar_contato', methods=['GET', 'POST'])
def adicionar_contato():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        codigo = len(contatos)
        contatos.append([codigo, nome, email, telefone])
        return redirect('/')
    else:
        return render_template('adicionar_contato.html')

@app.route('/editar_contato/<int:codigo>', methods=['GET', 'POST'])
def editar_contato(codigo):
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        contatos[codigo] = [codigo, nome, telefone, email]
        return redirect('/')  #Redireciona de volta para a página inicial
    else:
        contato = contatos[codigo]
        return render_template('editar_contato.html', contato=contato)  #Renderiza o formulário de edição

@app.route('/apagar_contato/<int:codigo>')
def apagar_contato(codigo):
    del contatos[codigo]
    return redirect('/')  #Redireciona de volta para a página inicial

if __name__ == '__main__':
    app.run(debug=True) #Executa o aplicativo flask