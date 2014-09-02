Channels
========

When it comes to channel data, like getting your stream key, game title and stream title. (Or even update them.) The order of the arguments doesn't matter.

get_channel()
-------------

With the **get_channel()** function, you can get the channel oject.

.. note::
	You can read more about **scopes** and how to obtain an **OAuth token** in the *Twitch API (v2) documentation*.

	You can find the documentation here: https://github.com/justintv/Twitch-API

::

	import pytwitch # pytwitch package
	import json # only used for pretty printing

	data = pytwitch.channels.get_channel(oauth='', name='')
	# Use json.dumps for pretty printing the response
	print(json.dumps(data, indent=4, sort_keys=True))

.. warning::
	You **can't** use both *oauth and name arguments* at the same time

	*required scope:* ``channel_read`` (only **oauth**)

If you provide an oauth access token, it will get you the authorized channel object back.

``oauth=''``

If you provide a name. It will get you the public channel object back.

``name=''``

set_channel()
---------------------

With the **set_channel()** function, you can set the title of your stream and/or the game title of your stream.

.. warning::
	**OAuth token is required** for the *set_channel()* function

	*required scope:* ``channel_editor``

::

	import pytwitch # pytwitch package
	import json # only used for pretty printing

	data = pytwitch.channels.set(oauth='', title='', game='')
	# Use json.dumps for pretty printing the JSON object you receive back
	print(json.dumps(data, indent=4, sort_keys=True))

Set the oauth token.

``oauth=''``

.. note::
	You arent *required* to use *both title and game argument*.

	Example: You only want to *update* the **title of the stream**. You simply only apply *oauth and title*.

Set the stream title.

``title=''``

Set the game title.

``game=''``

get_editors()
-------------

With the **get_editors()**, you can return all the editors of a channel

.. warning::
	**OAuth token is required** for the *get_editors()* function

	*required scope:* ``channel_read``

::

	import pytwitch # pytwitch package
	import json # only used for pretty printing

	data = pytwitch.channels.get_editors(oauth='')
	# Use json.dumps for pretty printing the JSON object you receive back
	print(json.dumps(data, indent=4, sort_keys=True))

Set the oauth token.

``oauth=''``
