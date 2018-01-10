from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():

    return render_template('index.html')


@app.route('/iniciar')
def iniciar_session():

    return render_template('iniciar_session/autentificacion.html')

@app.route('/visualizacion')
def visualizacion():

    return render_template('visualizacion_resultados/index.html')


if __name__ == '__main__':
    app.run()