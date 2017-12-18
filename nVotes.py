import os
from flask import Flask, request,  render_template, url_for, session, json
from flask.ext.session import Session
from jinja2 import Environment, PackageLoader, select_autoescape
from controllers import indexController, authController, censusMngController, votingMngController, votingBoothController

env = Environment(
    loader=PackageLoader('nVotes', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

app = Flask(__name__)
app.secret_key = os.urandom(24)
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
@app.route('/login')
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

@app.route('/census/create', methods=['GET'])
def createCensus():
	response = censusMngController.createCensus()
	return response

@app.route('/census/edit/<int:census_id>', methods=['GET'])
def showEditCensus(census_id):
	response = votingMngController.showEditCensus(census)
	return response

@app.route('/census/edit/<int:census_id>', methods=['POST'])
def editCensus(census_id):
	response = censusMngController.editVoting(census_id)
	return response

@app.route('/census/delete/<int:census_id>', methods=['GET'])
def deleteCensus(census_id):
	response = censusMngController.deleteCensus(census_id)
	return response

@app.route('/index/test')
def indexTest():
	data = {}
	data['var1'] = 'var1'
	data['var2'] = 'var2'
	response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
	return response


if __name__ == '__main__':
    app.run(debug=True, port=80)
