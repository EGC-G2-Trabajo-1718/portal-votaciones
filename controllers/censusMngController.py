from controllers.basecontroller import *

class CensusMngController(BaseController):

	def __init__(self):
		super().__init__(config.CENSUS_MNG_CONFIG['host'],
						 config.CENSUS_MNG_CONFIG['port'],
						 config.CENSUS_MNG_CONFIG['baseApi'],
						 config.CENSUS_MNG_CONFIG['baseTemplate'])


	def getCensus(self, census_id):
		data = {
			'id' : census_id
		}

		dataResponse = self.execRequest('/get', 'GET', data)

		if ((dataResponse['result'] != False)):
			response = dataResponse['content']
		else:
			response = {}

		return response

	def filterCensus(self, data):
		dataResponse = self.execRequest('/filter', 'GET', data)

		return dataResponse

	def listCensus(self):
		data = {}

		if request.args.get('id_votacion', None) != None:
			data['id_votacion'] = request.args.get('id_votacion')
		if request.args.get('id_grupo', None) != None:
			data['id_grupo'] = request.args.get('id_grupo')
		if request.args.get('nombre', None) != None:
			data['nombre'] = request.args.get('nombre')
		if request.args.get('fecha_ini', None) != None:
			data['fecha_ini'] = request.args.get('fecha_ini')
		if request.args.get('fecha_fin', None) != None:
			data['fecha_fin'] = request.args.get('fecha_fin')

		dataResponse = self.filterCensus(data)

		if ((dataResponse['result'] == False)):
			response = redirect(url_for('index'))
		else:
			template = self.templatePath('list.html')
			response = render_template(template, data=dataResponse['content'])

		return response

	def createForm(self):
		template = self.templatePath('createEditForm.html')

		return render_template(template, census=None, formUrl=url_for('createCensus'))

	def create(self):
		return redirect(url_for('listCensus'))

	def editForm(self, census_id):
		census = self.getCensus(census_id)
		fecha_ini = census['fecha_ini'].split(' ')
		fecha_ini_parts = fecha_ini[0].split('/')
		fecha_ini_parts.reverse()
		census['fecha_ini'] = '-'.join(fecha_ini_parts) + 'T' + fecha_ini[1]

		fecha_fin = census['fecha_fin'].split(' ')
		fecha_fin_parts = fecha_fin[0].split('/')
		fecha_fin_parts.reverse()
		census['fecha_fin'] = '-'.join(fecha_fin_parts) + 'T' + fecha_fin[1]

		template = self.templatePath('createEditForm.html')

		return render_template(template, census=census, formUrl=url_for('editCensus', census_id=census['id']))

	def edit(self, census_id):
		return request.form['fecha_fin']

	def deleteCensus(self, census_id):
		return 'Delete census id: ' + str(census_id)