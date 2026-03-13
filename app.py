from flask import Flask, render_template, redirect, request, flash
import requests

app = Flask(__name__)
app.secret_key = 'sun_key_777'

ENDPOINT_API = "https://api.thedogapi.com/v1/images/search"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/dog', methods=['POST'])
def dog():
    nome = request.form.get('nome', None)

    if not nome:
        flash('O NOME É NECESSÁRIO PARA ENCONTRAR UM AMIGO.')
        return redirect('/')
    
    try:
        # Busca um doguinho aleatório
        resposta = requests.get(ENDPOINT_API)
        dados = resposta.json()
        if dados:
            url_imagem = dados[0]['url']
            return render_template('index.html', nome=nome, url_imagem=url_imagem)
        else:
            flash('O SOL SE PÔS. TENTE NOVAMENTE.')
    except:
        flash('SISTEMA EM MANUTENÇÃO. OS CÃES ESTÃO PASSEANDO.')
    
    return redirect('/')

if __name__ == '__main__': 
    app.run(debug=True)