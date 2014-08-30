PyTwitch 0.0.1
===

No stable realease yet, however, I'll document my progress here. Until a stable release is ready.

Install
===

```bash
pip install pytwitch
```

Get Channel
===

```python
import pytwitch

# Gets own channel data (needs authentication)
json = pytwitch.get_channel()
# Gets specified channels public data
json = pytwitch.get_channel('channel_name')
print(json)
```