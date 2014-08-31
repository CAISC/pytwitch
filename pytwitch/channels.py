#!/usr/bin/env python

import requests, json

class Channels():
	def __init__(self):
		'''Get provided endpoints from Twitch'''
		r = requests.get('https://api.twitch.tv/kraken/')
		self.links = r.json()
		self.links = self.links['_links']
		self.headers = {
			'Accept': 'application/vnd.twitchtv.v2+json',
			'content-type': 'application/json',
		}

	def get(self, **kwargs):
		if kwargs.get('channel'):
			'''Get public users channel'''
			r = requests.get(self.links['channel']+'s/'+kwargs.get('channel'), headers=self.headers)
			data = r.json()
		elif kwargs.get('token'):
			'''Get authenticated users channel, scope: channel_read'''
			self.headers['Authorization'] = 'OAuth '+kwargs.get('token')
			r = requests.get(self.links['channel'], headers=self.headers)
			data = r.json()
		else:
			'''Error'''
			return 'See documentation...'
		return data

	def set(self, **kwargs):
		'''Default Payload'''
		payload = {
			'channel': {
				'status':'',
				'game':''
			}
		}

		if kwargs.get('token'):
			'''Get needed channel information'''
			self.headers['Authorization'] = 'OAuth '+kwargs.get('token')
			r = requests.get(self.links['channel'], headers=self.headers)
			data = r.json()
			payload['channel']['status'] = data['status']
			payload['channel']['game'] = data['game']
		else:
			return 'Error: Access token (token) wasn\'t set.'
		if kwargs.get('status'):
			'''Set the channels title/status'''
			payload['channel']['status'] = kwargs.get('status')
		if kwargs.get('game'):
			'''Set the channels game'''
			payload['channel']['game'] = kwargs.get('game')

		'''Send the data to be updated'''
		r = requests.put(data['_links']['self'], data=json.dumps(payload), headers=self.headers)
		return r.json()
