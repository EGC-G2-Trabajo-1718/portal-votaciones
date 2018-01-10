from flask import Flask , render_template
import parsingDeFicheros

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

@app.route('/listaEstilada')
def listaEstilada():
    return render_template('listaEstilada.html')

@app.route('/myVotes')
def myvotes():
    return render_template('listVotes.html')

@app.route('/vote')
def vote():
    censo = parsingDeFicheros.obtener_censo()
    votos = parsingDeFicheros.obtener_votantes()
    censo_y_votos = [censo, votos]
    opciones,votos = parsingDeFicheros.votosPorOpcion()
    return render_template('vote.html',opciones=opciones, votos=votos, censo_y_votos=censo_y_votos)

@app.route('/nationalityChart')
def nacionalityChart():
    ciudades,votos = parsingDeFicheros.parseLugaresGeograficos("ciudades")
    return render_template('nationalityChart.html',ciudades=ciudades, votos=votos)

@app.route('/ageChart')
def ageChart():
    rango,votos = parsingDeFicheros.parseEdades()
    return render_template('ageChart.html',edades=rango, recuento=votos)

@app.route('/hourChart')
def hourChart():
    tramos,votos = parsingDeFicheros.votosPorTramoHorario()
    return render_template('hourChart.html',tramos=tramos, votos=votos)


@app.route('/graficaEdad')
def graficaedad():
    rango,votos = parsingDeFicheros.parseEdades()
    return render_template('graficaEdad.html',edades=rango, recuento=votos)

@app.route('/graficaCiudad')
def graficaciudad():
    ciudades,votos = parsingDeFicheros.parseLugaresGeograficos("ciudades")
    return render_template('graficaCiudad.html',ciudades=ciudades, votos=votos)

@app.route('/graficaResultados')
def graficaResultados():
    opciones,votos = parsingDeFicheros.votosPorOpcion()
    return render_template('graficaResultados.html',opciones=opciones, votos=votos)

@app.route('/graficaHoras')
def graficaHoras():
    tramos,votos = parsingDeFicheros.votosPorTramoHorario()
    return render_template('graficaHoras.html',tramos=tramos, votos=votos)

@app.route('/grafica_censo_votos')
def graficaCensoYVotos():
    censo = parsingDeFicheros.obtener_censo()
    votos = parsingDeFicheros.obtener_votantes()
    censo_y_votos = [censo,votos]
    return render_template('votosPorCenso.html',censo_y_votos=censo_y_votos)


if __name__ == '__main__':
    app.run()
