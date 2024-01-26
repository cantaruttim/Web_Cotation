from flask import Flask, render_template
import requests

app = Flask(__name__)
@app.route('/')
def index():
    moedas = {
        'Dólar': get_cotacao('USD'),
        'Euro': get_cotacao('EUR'),
        'Libra': get_cotacao('GBP'),
        'Peso Argentino': get_cotacao('ARS')
    }
    return render_template('index.html', moedas=moedas)


def get_cotacao(moeda):
    link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    requisicao = requests.get(link)
    dic_requisicao = requisicao.json()
    cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
    return cotacao


if __name__ == "__main__":
    app.run(debug = True)