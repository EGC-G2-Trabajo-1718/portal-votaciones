from controllers.basecontroller import *

class IndexController(BaseController):

	def __init__(self):
		super().__init__('/', 'index/')


	def index(self):
		title = 'Index'
		return render_template(self.baseTemplatePath + 'index.html', title=title)
		#return super().callApi('http://127.0.0.1:5000/index/test', 'GET', {})['var1']