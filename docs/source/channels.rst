Channels
========

|  When it comes to channel data, like getting your **stream key**, **game** and channel **title**.
|  (Or even update them.) The **order** of the **arguments given**, does **NOT** matter.
|  

get_channel()
-------------

With the **get_channel()** function, you can get the channel oject.

.. note::
	|  You can read more about **scopes** and how to obtain an **OAuth token** in the *Twitch API (v2) documentation*.
	|  You can find the documentation here: https://github.com/justintv/Twitch-API
	|  

.. code-block:: python
	:emphasize-lines: 4,6

	import pytwitch # Import of PyTwitch.
	import json # Only imported to pretty print retuned JSON string.

	# Get the channel object either with OAuth or the name of the channel.
	data = pytwitch.channels.get_channel(oauth='', name='')
	# Pretty printing returned JSON object with json.dumps().
	print(json.dumps(data, indent=4, sort_keys=True))

.. warning::
	|  You **can't** use both *OAuth and name arguments* at the same time.
	|  *required scope(s):* ``channel_read`` (only for **OAuth** call.)
	|  

Arguments
^^^^^^^^^

.. code-block:: python

	# If you provide an oauth access token, it will get you the authorized channel object back.
	oauth=''

	# If you provide a name. It will get you the public channel object back.
	name=''

set_channel()
---------------------

|  With the **set_channel()** function, you can set the **title** of your channel
|  and/or the **game** of your channel.
|  

.. warning::
	|  **OAuth token is required** for the **set_channel()** function.
	|  *required scope(s):* ``channel_editor``
	|  

.. code-block :: python
	:emphasize-lines: 4,6

	import pytwitch # Import of PyTwitch.
	import json # Only used for pretty printing the returned JSON object.

	# Set the channels title and/or game, with OAuth
	data = pytwitch.channels.set(oauth='', title='', game='')
	# Pretty printing returned JSON object with json.dumps().
	print(json.dumps(data, indent=4, sort_keys=True))

.. note::
	|  You arent **required** to use **both** the **title** and **game** argument*.
	|  Example: You only want to **update** the **title** of the stream.
	|  You simply only provide the **OAuth** argument and the **title** argument.
	|  

Arguments
^^^^^^^^^

.. code-block:: python

	# Set the oauth token.
	oauth=''

	# Set the stream title.
	title=''

	# Set the game title.
	game=''

get_editors()
-------------

With the **get_editors()**, you can return all the editors of a channel

.. warning::
	|  **OAuth token is required** for the **get_editors()** function.
	|  *required scope(s):* ``channel_read``
	|  

.. code-block :: python
	:emphasize-lines: 4,6

	import pytwitch # Import of PyTwitch.
	import json # Only imported to pretty print retuned JSON string.

	# Get all the editors of channel with OAuth.
	data = pytwitch.channels.get_editors(oauth='')
	# Pretty printing returned JSON object with json.dumps().
	print(json.dumps(data, indent=4, sort_keys=True))

Arguments
^^^^^^^^^

.. code-block:: python

	# Set the oauth token.
	oauth=''
