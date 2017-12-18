from flask import Flask, request,  render_template, url_for, session, json
import requests

class BaseController:


	def __init__(self, baseApiUrl, baseTemplatePath):
		self.baseApiUrl = baseApiUrl
		self.baseTemplatePath = baseTemplatePath
		self.request = request

	
	def callApi(self, path, method, params):
		if method == 'POST':
			r = requests.post(path, params)
		else:
			r = requests.get(path, params)

		return r.json()
