# coding=utf-8
from flask import Flask , render_template
import parsingDeFicheros


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/graficaEdad')
def graficaedad():
    rango,votos = parsingDeFicheros.parseEdades()
    return render_template('graficaEdad.html',edades=rango, recuento=votos)




if __name__ == '__main__':
    app.run()
