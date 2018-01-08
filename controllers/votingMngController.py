from controllers.basecontroller import *

class VotingMngController(BaseController):

	def __init__(self):
		super().__init__(config.VOTING_MNG_CONFIG['host'],
						 config.VOTING_MNG_CONFIG['port'],
						 config.VOTING_MNG_CONFIG['baseApi'],
						 config.VOTING_MNG_CONFIG['baseTemplate'])

	def listVoting(self):
		return 'List voting'

	def createVoting(self):
		return 'Create voting'

	def showEditVoting(self, voting_id):
		session['voting_id'] = voting_id
		return 'Show edit voting form for voting id ' + str(session['voting_id'])

	def editVoting(self, voting_id):
		return 'Edit voting id ' + str(voting_id)

	def deleteVoting(self, voting_id):
		return 'Delete voting id ' + str(voting_id)