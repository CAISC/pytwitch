#!/usr/bin/env python

import requests, json

class Channels():
	def __init__(self):
		# Get provided base endpoints from the Twitch API
		r = requests.get('https://api.twitch.tv/kraken/')
		self.links = r.json()
		self.links = self.links['_links']
		self.headers = {
			'Accept': 'application/vnd.twitchtv.v2+json',
			'content-type': 'application/json',
		}
		self.error_temp = {
			'message': '',
			'status': ''
		}

	def __error(self, **kwargs):
		if kwargs.get('status') and kwargs.get('message'):
			self.error_temp['message'] = kwargs.get('message')
			self.error_temp['status'] = kwargs.get('status')
			return self.error_temp

	def get_channel(self, **kwargs):
		# Get kwargs and store them in a data dict
		data = {}
		for key, value in kwargs.items():
			data[key] = value

		if 'oauth' in data:
			# Set the OAuth header
			self.headers['Authorization'] = 'OAuth '+data['oauth']

		if 'oauth' in data or 'name' in data or 'editors' in data:
			# Get channel object by oauth or name
			if 'Authorization' in self.headers:
				r = requests.get(self.links['channel'], headers=self.headers)
			else:
				r = requests.get(self.links['channel']+'s/'+data['name'], headers=self.headers)
			# Set channel specific Twitch API endpoints		
			self.channel = r.json()
			self.channel_links = self.channel['_links']
			if 'editors' in data:
				# Editors True, get editors channel object instead of channel object
				r = requests.get(self.channel_links['editors'], headers=self.headers)
			# Return Channel Object
			return r.json()

		# Return a error if oauth or name or editors was given
		return self.__error(status='Error', message='See the documentation for useage.')

	def set_channel(self, **kwargs):
		# Default Payload
		payload = {
			'channel': {
				'status':'',
				'game':''
			}
		}

		# Get kwargs and store them in a data dict
		data = {}
		for key, value in kwargs.items():
			data[key] = value

		if 'oauth' in data:
			# Set the OAuth header
			self.headers['Authorization'] = 'OAuth '+data['oauth']
			# Get channel object by oauth
			r = requests.get(self.links['channel'], headers=self.headers)
			# Set channel specific Twitch API endpoints, title and game
			self.channel = r.json()
			self.title = self.channel['status']
			self.game = self.channel['game']
			self.channel_links = self.channel['_links']
		else:
			return self.__error(status='Authentication', message='Access token wasn\'t specified.')

		if 'title' in data:
			# If title specified add to the payload
			payload['channel']['status'] = data['title']
		else:
			payload['channel']['status'] = self.title

		if 'game':
			# If game specified add to the payload
			payload['channel']['game'] = data['game']
		else:
			payload['channel']['game'] = self.game

		# Send the data to be updated
		r = requests.put(self.channel_links['self'], data=json.dumps(payload), headers=self.headers)
		# Return the updated channel object
		return r.json()
