from controllers.basecontroller import *

class AuthController(BaseController):

	def __init__(self):
		super().__init__('/auth', 'auth/')



	def loginForm(self):
		title = 'Login'
		return render_template(self.baseTemplatePath + 'login.html', title=title, request=self.request)

	def login(self):
		title = 'Login'
		return render_template(self.baseTemplatePath + 'login.html', title=title, request=self.request)