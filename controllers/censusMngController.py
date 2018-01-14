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
			flash(u'Hubo un error en la conexion con el sistema de censos', 'error')
			response = redirect(url_for('index'))
		else:
			template = self.templatePath('list.html')
			response = render_template(template, data=dataResponse['content'])

		return response

	def createForm(self):
		template = self.templatePath('createEditForm.html')

		return render_template(template, census=None, formUrl=url_for('createCensus'))

	def create(self):
		data = {
			'id_votacion' : request.form['id_votacion'],
			'id_grupo': request.form['id_grupo']
		}

		if 'nombre' in request.form and len(request.form['nombre']) > 0:
			data['nombre'] = request.form['nombre']

		if 'fecha_ini' in request.form and len(request.form['fecha_ini']) > 0:
			data['fecha_ini'] = self.datetimeToApi(request.form['fecha_ini'])

		if 'fecha_fin' in request.form and len(request.form['fecha_fin']) > 0:
			data['fecha_fin'] = self.datetimeToApi(request.form['fecha_fin'])

		dataResponse = self.execRequest('/create', 'POST', data)

		if ((dataResponse['result'] == False)):
			flash(u'Hubo un error al eliminar el censo', 'error')
			response = redirect(url_for('listCensus'))
		elif ((dataResponse['result'] == True) and (dataResponse['content']['exito'] == 'true')):
			flash(u'Censo creado correctamente', 'success')
			response = redirect(url_for('listCensus'))
		else:
			template = self.templatePath('list.html')
			response = render_template(template, data=dataResponse['content'])

		return response


	def editForm(self, census_id):
		census = self.getCensus(census_id)

		if len(census) > 0:

			if 'fecha_ini' in census and len(census['fecha_ini']) > 0:
				census['fecha_ini'] = self.datetimeToHTML(census['fecha_ini'])

			if 'fecha_fin' in census and len(census['fecha_fin']) > 0:
				census['fecha_fin'] = self.datetimeToHTML(census['fecha_fin'])

			template = self.templatePath('createEditForm.html')
			response = render_template(template, census=census, formUrl=url_for('editCensus', census_id=census['id']))
		else:
			flash(u'El censo indicado no existe', 'error')
			response = redirect(url_for('index'))

		return response

	def edit(self, census_id):
		census = self.getCensus(census_id)

		if len(census) > 0:
			census['id_votacion'] = request.form['id_votacion']
			census['id_grupo'] = request.form['id_grupo']

			if 'nombre' in request.form and len(request.form['nombre']) > 0:
				census['nombre'] = request.form['nombre']
			else:
				if 'nombre' in census:
					del census['nombre']

			if 'fecha_ini' in request.form and len(request.form['fecha_ini']) > 0:
				census['fecha_ini'] = self.datetimeToApi(request.form['fecha_ini'])
			else:
				if 'fecha_ini' in census:
					del census['fecha_ini']

			if 'fecha_fin' in request.form and len(request.form['fecha_fin']) > 0:
				census['fecha_fin'] = self.datetimeToApi(request.form['fecha_fin'])
			else:
				if 'fecha_fin' in census:
					del census['fecha_fin']

			dataResponse = self.execRequest('/update', 'POST', census)

			if ((dataResponse['result'] == False)):
				flash(u'Hubo un error al eliminar el censo', 'error')
				response = redirect(url_for('listCensus'))
			elif ((dataResponse['result'] == True) and (dataResponse['content']['exito'] == 'true')):
				flash(u'Censo modificado correctamente', 'error')
				response = redirect(url_for('listCensus'))
			else:
				template = self.templatePath('list.html')
				response = render_template(template, data=dataResponse['content'])
		else:
			response = redirect(url_for('index'))

		return response

	def deleteCensus(self, census_id):
		data = {
			'id' : census_id
		}

		dataResponse = self.execRequest('/delete', 'GET', data)

		if ((dataResponse['result'] == False)):
			flash(u'Hubo un error al eliminar el censo', 'error')
			response = redirect(url_for('listCensus'))
		elif ((dataResponse['result'] == True) and (dataResponse['content']['exito'] == 'true')):
			flash(u'Censo eliminado correctamente', 'success')
			response = redirect(url_for('listCensus'))
		else:
			template = self.templatePath('list.html')
			response = render_template(template, data=dataResponse['content'])

		return response

	def datetimeToHTML(self, datetime):
		datetime_parts = datetime.split(' ')
		date_parts = datetime_parts[0].split('/')
		date_parts.reverse()
		datetime_format = '-'.join(date_parts) + 'T' + datetime_parts[1]

		return datetime_format

	def datetimeToApi(self, datetime):
		datetime_parts = datetime.split('T')
		date_parts = datetime_parts[0].split('-')
		date_parts.reverse()
		datetime_format = '/'.join(date_parts) + ' ' + datetime_parts[1]

		return datetime_format