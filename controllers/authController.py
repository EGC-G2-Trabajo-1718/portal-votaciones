from controllers.basecontroller import *

class AuthController(BaseController):

	def __init__(self):
		super().__init__('127.0.0.1', '5500', '/auth', 'auth/')



	def loginForm(self):
		title = 'Login'
		return render_template(self.baseTemplatePath + 'login.html', title=title)

	def login(self):
		title = 'Login'
		return render_template(self.baseTemplatePath + 'login.html')