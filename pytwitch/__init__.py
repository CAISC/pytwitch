#!/usr/bin/env python

__version__ = '0.0.1'

__twitch_api__ = {
	'api-url': 'https://api.twitch.tv/kraken/',
	'accept-header': 'application/vnd.twitchtv.v2+json'
}

from .api import get_channel
