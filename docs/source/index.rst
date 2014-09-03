PyTwitch Documentation |version_pypi|
=====================================

|  **PyTwitch** makes it easy to integrate the *Twitch API (v2)* into your own PyThon project.
|  It also has the added bonus of being able to integrate with the **StreamTip API**.

.. warning::
	|  The project is still **under heavy development** as of now, so only a **limited functionality**.
	|  Want to help? Fork the GitHub repository today at https://github.com/dhh-hss/pytwitch

Support and Badges
------------------

|  As of now **PyTwitch** only support |support|
|  It might work on prior versions of Python, but not **guaranteed**.
|  (There are plans to make this officially Python 2.7> compatible in the future.)

.. |support| image:: https://pypip.in/py_versions/pytwitch/badge.png
    :target: https://pypi.python.org/pypi/pytwitch
    :alt: Supported Python versions

Structure
---------

|  The structure used in this project, is heavily reflected on the actual *Twitch API (v2)* documentations.
|  You can learn more about the *Twitch API (v2)* here: https://github.com/justintv/twitch-api

JSON
----

|  All of the PyTwitch functions, even for error handling returns a JSON object right out of the box.
|  It's planned that PyTwitch in the future will support more than just a JSON object to be returned.
|
|  Status code 404 - Not Found
|  Status code 401 - Authentication error
|  Status code 200 - OK
|  Status code 101 - Fatal Error (function broke, probably not right arguments given)

Install
-------

``pip install pytwitch``

.. note::
	|  This will also **install requests**. **Requests** is an awesome Python package for making **HTTP(S) requests**.
	|  You can read more about **requests** at http://requests.readthedocs.org/

Contents
--------

.. toctree::
   :maxdepth: 3

   channels
   streamtip

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. |version_pypi| image:: https://pypip.in/version/pytwitch/badge.png
    :target: https://pypi.python.org/pypi/pytwitch
    :alt: Latest Version
