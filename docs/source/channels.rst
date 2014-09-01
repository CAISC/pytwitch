Channels
========

When it comes to channel data, like getting your stream key, game title and stream title. (Or even update them.) This is the main functions. The order of the arguments given doesn't matter. Replace .get/.set(arguments) with own arguments.

get_channel()
-------------

.. note::
	You can read more about scopes in the Twitch API v2 documentation, which you can find at https://github.com/justintv/Twitch-AP

::

	import pytwitch # pytwitch package
	import json # only used for pretty printing

	token = 'Your OAuth Token Key'

	# Will return an error, if no arguments given
	json = pytwitch.channels.get_channel(oauth=token, name='channel name', editors=True/False)
	# Use json.dumps for pretty printing
	print(json.dumps(json, indent=4, sort_keys=True))

get_channel() arguments
-----------------------

If you provide an oauth access token, it will get you authorized channel object back.

.. warning::
	This method will not do anything with the ``name`` argument, channel_read scope is needed.

	``oauth='your access token'``

If you provide a name. It will get you the public channel object back.

	``name='test_user1'``

If you use the editors argument, it will instead return all the users that have editor permission on the channel.

.. warning::
	This argument requires the channel_read scope and therefor a oauth key, see the oauth argument section above

	``editors=True``

set_channel()
-------------

With the set function, you can set the title of your stream and/or the game title of your stream.

.. warning::
	OAuth token is required for the set_channel function

::

	import pytwitch # pytwitch package
	import json # only used for pretty printing

	token = 'Your OAuth Token Key'

	# Will return an error, no arguments given
	parsed = pytwitch.channels.set(oauth=token, title='My awesome Stream Title', game='Game Title')
	# Use json.dumps for pretty printing the JSON object you receive back
	print(json.dumps(parsed, indent=4, sort_keys=True))

set_channel() arguments
-----------------------

Set the oauth token.

	``oauth='your access token'``

Set the stream title.

	``title='My awesome new Stream Title'``

Set the game title.

	``game='Game Title'``
