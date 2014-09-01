Channels
========

When it comes to channel data, like getting your stream_key and game title and stream title. (Or even update them.) This is the main functions. The order of the arguments given doesn't matter. Replace .get/.set(arguments) with own arguments.

Get channel data
----------------

::

	import pytwitch # pytwitch package
	import json # only used for pretty printing

	access_token = 'Your Access Token'

	# Will return an error, no arguments given
	parsed = pytwitch.Channels().get(arguments)
	# Use json.dumps for pretty printing
	print(json.dumps(parsed, indent=4, sort_keys=True))

If you provide an access token, it will get the access token's provided JSON object. In other words, the owner of the access token. Information like the stream key is also obtained this way.

    ``token=access_token``

If you instead want to get a channels data by providing the channel='name', you will get all the public data avaiable for that channel.

    ``channel='test_user1'``

Only one of the arguments (token or channel) can be provided at a given time.

Set channel data
----------------

With the set function, you can set the title of your stream and/or the game title of your stream.
This requires authentication aka. access_token to work.

::

	import pytwitch # pytwitch package
	import json # only used for pretty printing

	access_token = 'Your Access Token'
	# Will return an error, no arguments given
	parsed = pytwitch.Channels().set(arguments)
	# Use json.dumps for pretty printing the JSON object you receive back
	print(json.dumps(parsed, indent=4, sort_keys=True))

The access token to authenticate (required)

    ``token=access_token (token='string')``

Set the stream title

    ``status='My awesome new Stream Title'``

Set the game title

    ``game='Hearthstone: Heroes of Warcraft'``
