#!/usr/bin/env python

import requests
from .utils import Utils
utils = Utils()

class StreamTip():
	def __init__(self):
		self.endpoints = {
			'tips': 'https://streamtip.com/api/tips',
			'tips/csv': 'https://streamtip.com/api/tips/csv'
		}
		self.payload = {
			'direction': 'asc',
			'limit': '25',
			'offset': '0',
			'sort_by': 'date'
		}
		self.headers = {
			'Authorization': '',
			'content-type': 'application/json'
		}

	def get_tips(self, **kwargs):
		# Get kwargs and store them in a data dict
		data = utils.data(kwargs)

		# Check if client-id and access-token are present
		if 'client_id' in data and 'access_token' in data:
			self.headers['Authorization'] = data['client_id']+' '+data['access_token']
		else:
			return utils.error(error='Unauthorized', message='client_id and access_token are required', status=401)

		# Check for different query arguments
		for key in self.payload:
			if key in data:
				self.payload[key] = data[key]

		# Get the tips
		r = requests.get(self.endpoints['tips'], params=self.payload, headers=self.headers)
		if r.json()['status'] == 401:
			return utils.error(error='Unauthorized', message='client_id and/or access_token was invalid', status=401)
		return r.json()
