PyTwitch 0.0.1
==============

This is the description file for the project.

Get Channel
===========

```python
import pytwitch

# Gets own channel data (needs authentication)
json = pytwitch.get_channel()
# Gets specified channels public data
json = pytwitch.get_channel('channel_name')
print(json)
```