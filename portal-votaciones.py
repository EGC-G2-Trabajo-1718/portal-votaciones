from flask import Flask , render_template
import parsingDeFicheros

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

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
    censo = parsingDeFicheros.obtener_censo(None, None)
    votos = parsingDeFicheros.obtener_votantes(None, None)
    censo_y_votos = [censo, votos]
    opciones,votos = parsingDeFicheros.votosPorOpcionNuevaApi(None,None)
    return render_template('vote.html',opciones=opciones, votos=votos, censo_y_votos=censo_y_votos)

@app.route('/cityChart')
def cityChart():
    ciudades,votos = parsingDeFicheros.parseLugaresGeograficos("ciudades")
    return render_template('cityChart.html',ciudades=ciudades, votos_ciudad=votos)

@app.route('/nationalityChart')
def nacionalityChart():
    paises,votos = parsingDeFicheros.parseLugaresGeograficos("paises")
    return render_template('nationalityChart.html',paises=paises, votos_pais=votos)

@app.route('/ageChart')
def ageChart():
    rango,votos = parsingDeFicheros.parseEdades()
    return render_template('ageChart.html',edades=rango, votos_edad=votos)

@app.route('/hourChart')
def hourChart():
    tramos,votos = parsingDeFicheros.votosPorTramoHorario()
    return render_template('hourChart.html',tramos=tramos, votos_horas=votos)

@app.route('/moreChart')
def moreChart():
    tramos,votos_horas = parsingDeFicheros.votosPorTramoHorario()
    rango, votos_edad = parsingDeFicheros.parseEdades()
    paises, votos_pais = parsingDeFicheros.parseLugaresGeograficos("paises")
    ciudades, votos_ciudad = parsingDeFicheros.parseLugaresGeograficos("ciudades")
    return render_template('moreChart.html',tramos=tramos, paises=paises, edades=rango, ciudades=ciudades, votos_horas=votos_horas, votos_edad=votos_edad, votos_ciudad=votos_ciudad, votos_pais=votos_pais)


if __name__ == '__main__':
    app.run()
