from flask import Flask, request, render_template, url_for, session, json, redirect
from controllers import config
import requests

class BaseController:


	def __init__(self, host, port, baseApiUrl, baseTemplatePath):
		self.host = host
		self.port = port
		self.baseApiUrl = baseApiUrl
		self.baseTemplatePath = baseTemplatePath
		self.request = request

	def getApiUrl(self):
		url = self.host

		if self.port != 80:
			url = url + ':' + self.port

		url = url + self.baseApiUrl

		return url

	def templatePath(self, template):
		templatePath = self.baseTemplatePath + '/' + template

		return templatePath

	def execRequest(self, path, method, payload):
		url = self.getApiUrl() + path
		response = ''
		try:
			if method == 'POST':
				r = requests.post(url, data=payload)
			elif method == 'GET':
				r = requests.get(url, params=payload)
			else:
				r = requests.request(method, url, params=payload)

			if r.status_code != 200:
				raise requests.exceptions.ConnectionError

			try:
				content = r.json()
				response = {'result': True, 'content': content}
			except ValueError:
				content = r.text
				response = {'result': True, 'content': content}
		except requests.exceptions.ConnectionError:
			response = {'result': False, 'message' : 'Connection error!', 'request' : r}

		return response
