#!/usr/bin/env python

class Utils():
	def data(self, kwargs):
		data = {}
		for key, value in kwargs.items():
			data[key] = value
		return data

	def error(self, **kwargs):
		error_temp = {}
		data = self.data(kwargs)
		if 'status' in data and 'message' in data:
			error_temp['error'] = data['error']
			error_temp['message'] = data['message']
			error_temp['status'] = data['status']
			return error_temp

	def pretty_header(self, header):
		if header:
			return print(header+'\n'+'=' * len(header))

	def convert_to_iso(self, arg):
		return arg.isoformat()
