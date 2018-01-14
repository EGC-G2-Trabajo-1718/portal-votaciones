import os
import binascii
from flask import Flask, request,  render_template, url_for, session, json
from flask.ext.session import Session
from jinja2 import Environment, PackageLoader, select_autoescape
from controllers import indexController, authController, censusMngController, votingMngController, votingBoothController
import parsingDeFicheros

env = Environment(
    loader=PackageLoader('nVotes', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

app = Flask(__name__)
app.config.from_pyfile('config.py')
Session(app)


indexController = indexController.IndexController()
authController = authController.AuthController()
votingMngController = votingMngController.VotingMngController()
censusMngController = censusMngController.CensusMngController()
votingBoothController = votingBoothController.VotingBoothController()


"""
	Index routes
"""
@app.route('/')
def index():
	response = indexController.index()
	return response


"""
	Auth routes
"""
@app.route('/login', methods=['GET'])
def loginForm():
	response = authController.loginForm()
	return response

@app.route('/login', methods=['POST'])
def login():
	response = authController.login()
	return response



"""
 	Voting management routes
"""

@app.route('/voting', methods=['GET'])
def listVoting():
	response = votingMngController.listVoting()
	return response

@app.route('/voting/create', methods=['GET'])
def createVoting():
	response = votingMngController.createVoting()
	return response

@app.route('/voting/edit/<int:voting_id>', methods=['GET'])
def showEditVoting(voting_id):
	response = votingMngController.showEditVoting(voting_id)
	return response

@app.route('/voting/edit/<int:voting_id>', methods=['POST'])
def editVoting(voting_id):
	response = votingMngController.editVoting(voting_id)
	return response

@app.route('/voting/delete/<int:voting_id>', methods=['GET'])
def deleteVoting(voting_id):
	response = votingMngController.deleteVoting(voting_id)
	return response


"""
 	Censuses management routes
"""

@app.route('/census', methods=['GET'])
def listCensus():
	response = censusMngController.listCensus()
	return response

@app.route('/census/<int:census_id>', methods=['GET'])
def getCensus(census_id):
	response = censusMngController.getCensus(census_id)
	return response

@app.route('/census/create', methods=['GET'])
def createCensusForm():
	response = censusMngController.createForm()
	return response

@app.route('/census/create', methods=['POST'])
def createCensus():
	response = censusMngController.create()
	return response

@app.route('/census/edit/<int:census_id>', methods=['GET'])
def editCensusForm(census_id):
	response = censusMngController.editForm(census_id)
	return response

@app.route('/census/edit/<int:census_id>', methods=['POST'])
def editCensus(census_id):
	response = censusMngController.edit(census_id)
	return response

@app.route('/census/delete/<int:census_id>', methods=['GET'])
def deleteCensus(census_id):
	response = censusMngController.deleteCensus(census_id)
	return response


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
    return render_template('cityChart.html',ciudades=ciudades, votos=votos)

@app.route('/nationalityChart')
def nacionalityChart():
    paises,votos = parsingDeFicheros.parseLugaresGeograficos("paises")
    return render_template('nationalityChart.html',paises=paises, votos=votos)

@app.route('/ageChart')
def ageChart():
    rango,votos = parsingDeFicheros.parseEdades()
    return render_template('ageChart.html',edades=rango, recuento=votos)

@app.route('/hourChart')
def hourChart():
    tramos,votos = parsingDeFicheros.votosPorTramoHorario()
    return render_template('hourChart.html',tramos=tramos, votos=votos)


if __name__ == '__main__':
	app.run(debug=True, port=80)
