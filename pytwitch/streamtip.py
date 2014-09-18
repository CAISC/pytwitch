#!/usr/bin/env python

import requests, json
from .utils import Utils
utils = Utils()

class StreamTip():
	def __init__(self):
		# Set BASE endpoint(s) for future navigation
		self.endpoints = {
			'tips': 'https://streamtip.com/api/tips'
		}

	def get_tips(self, **kwargs):
		# Default values, set every time you call the function
		self.payload = {
			'date_from': '2013-06-07T04:20:43.818Z',
			'direction': 'desc',
			'limit': 25,
			'offset': 0,
			'sort_by': 'date'
		}
		# Default headers, set every time the function is called
		self.headers = {
			'Authorization': '',
			'content-type': 'application/json'
		}

		# Get kwargs and store them in a data dict
		data = utils.data(kwargs)

		# Check if client-id and access-token are present
		if 'client_id' in data and 'access_token' in data:
			self.headers['Authorization'] = data['client_id']+' '+data['access_token']
		else:
			return utils.error(error='Unauthorized', message='client_id and access_token are required', status=401)

		# Check for short handlers, this ommits other query arguments
		if 'get' in data:
			data['get'] = str.lower(data['get'])
			self.payload['limit'] = 1
			if 'top' in data['get']:
				self.payload['sort_by'] = 'amount'
			elif 'recent' in data['get']:
				self.payload['sort_by'] = 'date'
			else:
				return utils.error(error='Fatal Error', message='Only top and recent are valid shorthandler arguments', status=101)
		else:
			# Check query arguments for none valid values

			if 'sort_by' in data:
				data['sort_by'] = str.lower(data['sort_by'])
				if 'amount' in data['sort_by'] or 'date' in data['sort_by']:
					pass
				else:
					return utils.error(
						error='Fatal Error',
						message='sort_by="'+data['sort_by']+'" -  Valid Values: \'date\', \'amount\'. (str) ie,. sort_by="amount"',
						status=101)
			if 'direction' in data:
				data['direction'] = str.lower(data['direction'])
				if 'asc' in data['direction'] or 'desc' in data['direction']:
					pass
				else:
					return utils.error(
						error='Fatal Error',
						message='directon="'+data['direction']+'" - Valid Values: \'asc\', \'desc\'. (str) ie,. direction="desc"',
						status=101)
			if 'offset' in data:
				if isinstance(data['offset'], int) and 0 <= data['offset'] <= 100:
					pass
				else:
					return utils.error(
						error='Fatal Error',
						message='offset='+str(data['offset'])+' - Valid Values: 1-25. (int) ie,. offset=1',
						status=101)
			if 'limit' in data:
				if isinstance(data['limit'], int) and 1 <= data['limit'] <= 25:
					pass
				else:
					return utils.error(
						error='Fatal Error',
						message='limit='+str(data['limit'])+' - Valid Arguments: 1-100. (int) ie,. limit=25',
						status=101)

			# Set query (payload) for different valid arguments and values
			for key in self.payload:
				if key in data:
					self.payload[key] = data[key]

		# Get the tips
		r = requests.get(self.endpoints['tips'], params=self.payload, headers=self.headers)
		if r.status_code == 200:
			return r.json()
		else:
			return utils.error(error=r.json()['message'],
				message="Client ID and/or Access Token wasn't valid.",
				status=r.json()['status'])
