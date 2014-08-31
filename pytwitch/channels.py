#!/usr/bin/env python

import requests

class Channels():
	def __init__(self):
		'''Get provided endpoints from Twitch'''
		r = requests.get('https://api.twitch.tv/kraken/')
		self.links = r.json()
		self.links = self.links['_links']

	def get(self, **kwargs):
		if kwargs.get('channel'):
			'''Get public users channel'''
			r = requests.get(self.links['channel']+'s/'+kwargs.get('channel'))
			data = r.json()
		elif kwargs.get('token'):
			'''Get authenticated users channel, scope: channel_read'''
			r = requests.get(self.links['channel']+'?oauth_token='+kwargs.get('token'))
			data = r.json()
		else:
			'''Error'''
			return 'See documentation...'
		return data
