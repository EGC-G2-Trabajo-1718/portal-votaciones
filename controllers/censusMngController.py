from controllers.basecontroller import *

class CensusMngController(BaseController):

	def __init__(self):
		super().__init__('/administracionCensos', 'census_management')


	def listCensus(self):
		return 'List census'

	def createCensus(self):
		return 'Create census'

	def showEditCensus(self, census_id):
		return 'Show edit census form for census id: ' + str(census_id)

	def editCensus(self, census_id):
		return 'Edit census id: ' + str(census_id)

	def deleteCensus(self, census_id):
		return 'Delete census id: ' + str(census_id)