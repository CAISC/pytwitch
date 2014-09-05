PyTwitch Documentation (|release|) |version_pypi|
=================================================

|  **PyTwitch** makes it easy to integrate the *Twitch API (v2)* into your own PyThon project.
|  It also has the added bonus of being able to integrate with the **StreamTip API**.
|  

.. warning::
	|  The project is still **under heavy development** as of now, so only a **limited functionality**.
	|  Want to help? Fork the GitHub repository today at https://github.com/dhh-hss/pytwitch
	|

Python Support
--------------

|  As of now **PyTwitch** only supports *(officially)* **Python 3.2>**.
|  It **might** work on *prior versions* of **Python**, but not **guaranteed**.
|  
|  (There are plans to make **PyTwitch officially** work with **Python 2.7>** in the future.)
|  

Install
-------

.. code-block :: bash

	$ pip install pytwitch

.. note::
	|  This will also **install requests**. **Requests** is an awesome **Python Package**
	|  for making **HTTP(S) requests**.
	|  You can read more about **requests** at http://requests.readthedocs.org/
	|  

Structure
---------

|  The structure used in this project, is heavily reflected on the actual *Twitch API (v2)* documentations.
|  You can learn more about the *Twitch API (v2)* here: https://github.com/justintv/twitch-api
|  

JSON Responses?
---------------

|  All of the PyTwitch functions, even for error handling returns a JSON object right out of the box.
|  It's planned that PyTwitch in the future will support more than just a JSON object to be returned.
|  

Example Error Response
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: json
	:emphasize-lines: 5,7

	# Example get_channel() JSON response
	{
	  'error': 'Fatal Error'
	  'message': 'get_channel: See the PyTwtich documentation for useage.'
	  'status': 101
	}

Status Codes
^^^^^^^^^^^^

|  404 = Not Found
|  401 = Unauthorized
|  200 = OK
|  101 = Fatal Error
|  

Contents
--------

.. toctree::
   :maxdepth: 3

   channels
   streamtip

.. |version_pypi| image:: https://pypip.in/version/pytwitch/badge.png
    :target: https://pypi.python.org/pypi/pytwitch
    :alt: Latest Version
