#!/usr/bin/env python

import json

class Utils():
	def data(self, kwargs):
		data = {}
		for key, value in kwargs.items():
			data[key] = value
		return data

	def error(self, **kwargs):
		error_temp = {}
		data = self.data(kwargs)
		if 'error' in data:
			error_temp['error'] = data['error']
		else:
			error_temp['error'] = ''
		if 'message' in data:
			error_temp['message'] = data['message']
		else:
			error_temp['message'] = ''
		if 'status' in data:
			error_temp['status'] = data['status']
		else:
			error_temp['status'] = ''
		return error_temp

	def pretty_header(self, text, *underline):
		if text and underline:
			underline = underline[0]
		else:
			underline = '='
		return print(text+'\n'+underline * len(text))

	def pretty_json(self, data):
		if data:
			return print(json.dumps(data, indent=4, sort_keys=True)+'\n')
		else:
			return print(self.error(error='No Data',
				message='You did not specify JSON data source to be pretty printed.',
				status=101))
