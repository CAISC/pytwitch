#!/usr/bin/env python

import requests, json
from .utils import Utils
utils = Utils()

class Channels():
	def __init__(self):
		# Get provided base endpoints from the Twitch API
		r = requests.get('https://api.twitch.tv/kraken/')
		# Check if the API is available
		if r.status_code != 200:
			# Return Error
			return utils.error(
				error='Servce Unavailable',
				message='Twitch (v2) API seems to be down, try again later.',
				status=503
			)
		else:
			# Set BASE endpoints provided by Twitch for easy navigation
			self.base_endpoints = r.json()['_links']
			# Set BASE (default) header values
			self.headers = {
				'Accept': 'application/vnd.twitchtv.v2+json',
				'content-type': 'application/json'
			}
			# Set BASE payload (parameters) for set_channel() function
			self.payload = {'channel':{}}

	def get_channel(self, **kwargs):
		# Get kwargs and store them in a data dict
		data = utils.data(kwargs)

		if 'oauth' in data:
			# Set the OAuth header
			self.headers['Authorization'] = 'OAuth '+data['oauth']
			# Get the OAuth channel object
			r = requests.get(self.base_endpoints['channel'], headers=self.headers)
		if 'name' in data:
			# Get channel object by name (public)
			r = requests.get(self.base_endpoints['channel']+'s/'+data['name'], headers=self.headers)
		# Return Channel Object
		if r.status_code == 200:
			return r.json()

		# Return a error if none of the arguments was met
		return utils.error(error='Fatal Error', message='get_channel: See the PyTwtich documentation for useage.', status=101)

	def set_channel(self, **kwargs):
		# Get kwargs and store them in a data dict
		data = utils.data(kwargs)

		if 'oauth' in data:
			# Set the OAuth header
			self.headers['Authorization'] = 'OAuth '+data['oauth']
			# Get channel object by oauth
			r = requests.get(self.base_endpoints['channel'], headers=self.headers)
		else:
			utils.error(error='Unauthorized', message='OAuth is requried, see documentation', status=401)

		if 'title' in data or 'game' in data:
			# If title or game specified add to the payload
			if 'title' in data:
				self.payload['channel']['status'] = data['title']
			if 'game' in data:
				self.payload['channel']['game'] = data['game']
			# Send the data to be updated
			r = requests.put(self.base_endpoints['channel'], data=json.dumps(self.payload), headers=self.headers)
			# Return the updated channel object
			return r.json()

		# Return a error if none of the arguments was met
		return utils.error(error='Fatal Error', message='set_channel: See the PyTwtich documentation for useage.', status=101)

	def get_editors(self, **kwargs):
		# Get kwargs and store them in a data dict
		data = utils.data(kwargs)

		if 'oauth' in data:
			# Set the OAuth header
			self.headers['Authorization'] = 'OAuth '+data['oauth']
			r = requests.get(self.base_endpoints['channel'], headers=self.headers)
			# Check for errors
			if r.json()['status'] == 401:
				return r.json()
			# Set channel specific Twitch API endpoints		
			self.channel_endpoints = r.json()['_links']
			
			# Get editors json object
			r = requests.get(self.channel_endpoints['editors'], headers=self.headers)
			return r.json()
		else:
			utils.error(error='Unauthorized', message='OAuth is requried, see documentation', status=401)

		# Return a error if none of the arguments was met
		return utils.error(error='Fatal Error', message='get_editors: See the PyTwtich documentation for useage.', status=101)
