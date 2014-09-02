StreamTip
=========

Easily get you latest tips (donations) through the StreamTip API. (http://streamtip.com)

get_tips()
-------------

With the **get_tips()** function, you can retrieve tips (donations) with a **client_id** and **access_token**.

.. note::
	You can find your *client_id* and *access_token* by logging into http://streamtip.com and go to your *account*. (https://streamtip.com/account/billing)

.. warning::
	(Taken from the StreamTip API documentation)

	``Do not place calls to these APIs on a publicly accessible website!``

	Your ``client_id`` and ``access_token`` must remain confidential to ensure the security of your account. **An opt-in, publicly accessible solution with more limited data (personal info removed) will be coming sometime in the future for those who need it.**

::

	import pytwitch

	data = pytwitch.streamtip.get_tips(client_id='', access_token='')
	print(json.dumps(data, indent=4, sort_keys=True)+'\n')

The direction results are returned. (**asc** or **desc**, default value is **asc**)

``direction=''``

The number of items to be returned. (default value is **25**)

``limit=''``

The number of items to skip. (default value is **0**)

``offset=''``

The field to sort by. (**date** and **amount** are supported, default value is **date**)

``sort_by=''``
