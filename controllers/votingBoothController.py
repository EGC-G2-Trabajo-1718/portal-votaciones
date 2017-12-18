from controllers.basecontroller import *

class VotingBoothController(BaseController):

	def __init__(self):
		super().__init__('/cabinaVotaciones', 'voting_booth')

	