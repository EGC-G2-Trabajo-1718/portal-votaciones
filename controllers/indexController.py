from controllers.basecontroller import *

class IndexController(BaseController):

	def __init__(self):
		super().__init__(config.INDEX_CONFIG['host'],
						 config.INDEX_CONFIG['port'],
						 config.INDEX_CONFIG['baseApi'],
						 config.INDEX_CONFIG['baseTemplate'])


	def index(self):
		title = 'Index'
		template = self.templatePath('index.html')
		return render_template(template, title=title)