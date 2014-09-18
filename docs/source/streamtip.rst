StreamTip
=========

|  Easily get your latest tips (donations) through the *StreamTip API*.
|  You can learn more about the *StreamTip* API at (http://streamtip.com)
|  (You **have** to be **logged in** to see the *API documentation*.)
|  

get_tips()
-------------

With the **get_tips()** function, you can retrieve tips (donations) with a **client_id** and **access_token**.

.. note::
	|  You can find your **client_id** and **access_token** by logging into http://streamtip.com
	|  and go to your *account*. (https://streamtip.com/account/billing)
	|  

.. danger::
	|  (Taken from the *StreamTip API* documentation)
	|
	|  **Do not place calls to these APIs on a publicly accessible website!**
	|
	|  Your **client_id and access_token** must remain confidential to ensure the security of your account. 
	|  **An opt-in, publicly accessible solution with more limited data (personal info removed) will be coming**
	|  **sometime in the future for those who need it.**
	|  

Example
^^^^^^^

.. code-block:: python

	import pytwitch # Import of PyTwitch.

	# Getting 25 latest tips (default) sorted by date and in desc (descending) order.
	# If you only provide required client_id and access_token.
	data = pytwitch.streamtip.get_tips(client_id="<client id>", access_token="<access token>")
	# Pretty printing JSON for debugging purposes using utils.pretty_json
	pytwitch.utils.pretty_json(data)

Arguments
^^^^^^^^^

.. code-block:: python

	# OAuth (required)
	client_id=""
	access_token=""

	# Shortcut argument, ommits all other arguments other than the required client_id and access_token
	# top - Gets all time top tipper/donator
	# recent - Gets the most recent tipper/donator
	get=""

	# The direction tips are returned. (**asc** or **desc**, default value is **asc**)
	direction=""

	# The number of tips to be returned. (default value is **25**)
	limit=""

	# The number of tips to skip. (default value is **0**)
	offset=""

	# The field to sort tips by. (**amount** and **date** are supported, default value is **date**)
	sort_by=""
