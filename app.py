from flask import Flask, render_template, request, redirect
import os


#Cria uma classe
class Carne:
    def __init__(self, peca, categoria, preco, imagem):
        self.peca = peca
        self.categoria = categoria
        self.preco = preco
        self.imagem = imagem

carne1 = Carne('Tulipa', 'Ave', '29,90', '/static/img/Tulipa_frango.png')
carne2 = Carne('Fraldinha', 'Bovino', '50.90', '/static/img/picanha.jpg')
carne3 = Carne('Panceta', 'Suino', '40,90', '/static\img\File_frango.jpg')
lista = [carne1, carne2, carne3]

app = Flask(__name__)

UPLOAD_FILE = "static/img"
app.config[UPLOAD_FILE] = UPLOAD_FILE

@app.route('/')
def index():
    return render_template('index.html', nomeLoja='Los Pollos Hermanos', cat=lista)


#Criando uma nova rota
@app.route('/cadastro')
def novo():
    return render_template('cadastro_prod.html', titulo='Carne nova')


@app.route('/criar', methods=['POST', ])
def criar():
    peca = request.form['peca']
    categoria = request.form['categoria']
    preco = request.form['preco']
    imagem = request.files.get('imagem')

    imagem_url = ''

    if imagem and imagem.filename != '':
        filename = os.path.join(app.config[UPLOAD_FILE], imagem.filename)
        imagem.save(filename)
        imagem_url = f'/static/img/{imagem.filename}'

    carne = Carne(peca, categoria, preco, imagem_url)
    lista.append(carne)
    return redirect('/')


app.run(debug=True)
