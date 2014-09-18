Channels
========

|  When it comes to channel data, like getting your **stream key**, **game** and channel **title**.
|  (Or even update them.) The **order** of the **arguments given**, does **NOT** matter.
|

.. note::
	|  You can read more about **scopes** and how to obtain an **OAuth token** in the *Twitch API (v2) documentation*.
	|  Link to authentication section: https://github.com/justintv/Twitch-API/blob/master/authentication.md
	|  Direct link to scopes: https://github.com/justintv/Twitch-API/blob/master/authentication.md#scope
	|  

get_channel()
-------------

With the **get_channel()** function, you can get the channel oject.

Example
^^^^^^^

.. code-block:: python

	import pytwitch # Import of PyTwitch.

	# Get the channel object either with OAuth or the name of the channel.
	data = pytwitch.channels.get_channel(oauth="<oauth>", name="<test_user1>")
	# Pretty printing JSON for debugging purposes using utils.pretty_json()
	pytwitch.utils.pretty_json(data)

.. warning::
	|  You **can't** use both *OAuth and name arguments* at the same time.
	|  *required scope(s):* ``channel_read`` (only for **OAuth** call.)
	|  

Arguments
^^^^^^^^^

.. code-block:: python

	# If you provide an oauth access token, 
	# it will get you the authorized channel object back.
	oauth=""
  
	# If you provide a name, it will get you the public channel object back.
	name=""

set_channel()
---------------------

|  With the **set_channel()** function, you can set the **title** of your channel
|  and/or the **game** of your channel.
|  

.. warning::
	|  **OAuth token is required** for the **set_channel()** function.
	|  *required scope(s):* ``channel_editor``
	|  

Example
^^^^^^^

.. code-block :: python

	import pytwitch # Import of PyTwitch.

	# Set the channels title and/or game, with OAuth
	data = pytwitch.channels.set(oauth="<oauth token>", title="<title>", game="<game>")
	# Pretty printing JSON for debugging purposes using utils.pretty_json()
	pytwitch.utils.pretty_json(data)

.. note::
	|  You arent **required** to use **both** the **title** and **game** argument*.
	|  Example: You only want to **update** the **title** of the stream.
	|  You simply only provide the **oauth** argument and the **title** argument.
	|  

Arguments
^^^^^^^^^

.. code-block:: python

	# Set the oauth token.
	oauth=""

	# Set the stream title.
	title=""

	# Set the game title.
	game=""

get_editors()
-------------

With the **get_editors()**, you can return all the editors of a channel

.. warning::
	|  **OAuth token is required** for the **get_editors()** function.
	|  *required scope(s):* ``channel_read``
	|  

Example
^^^^^^^

.. code-block :: python

	:emphasize-lines: 5,7

	import pytwitch # Import of PyTwitch.
	import json # Only imported to pretty print retuned JSON string.

	# Get all the editors of channel with OAuth.
	data = pytwitch.channels.get_editors(oauth="<ouath>")
	# Pretty printing JSON for debugging purposes using utils.pretty_json()
	pytwitch.utils.pretty_json(data)

Arguments
^^^^^^^^^

.. code-block:: python

	# Set the oauth token.
	oauth=""
