from controllers.basecontroller import *

class VotingBoothController(BaseController):

	def __init__(self):
		super().__init__(config.VOTING_BOOTH_CONFIG['host'],
						 config.VOTING_BOOTH_CONFIG['port'],
						 config.VOTING_BOOTH_CONFIG['baseApi'],
						 config.VOTING_BOOTH_CONFIG['baseTemplate'])

	