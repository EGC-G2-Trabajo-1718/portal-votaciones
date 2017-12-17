from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return 'Hello world!'


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')


if __name__ == '__main__':
    app.run()
