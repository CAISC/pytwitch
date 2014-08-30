#!/usr/bin/env python

from pytwitch import __twitch_api__
import requests

def get_channel(channel=None):
	if not channel:
		return 'Do something with auth here...'
	else:
		'''Get specified users channel'''
		r = requests.get(__twitch_api__['api-url']+'channels/'+channel)
		return r.json()
