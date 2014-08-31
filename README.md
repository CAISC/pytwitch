PyTwitch 0.0.1
===

No stable realease yet, however, I'll document my progress here. Until a stable release is ready.

Install
===

You can't install pytwitch yet, this is just the documentation for it!

```bash
pip install pytwitch
```

Channels
===

__Index__

- Authorized Channel Data
- Public Channel Data

Authorized Channel Data
---

```python
import pytwitch # pytwitch package
import json # only used for pretty printing

token = 'Your Access Token'

parsed = pytwitch.Channels().get(token=token)
# Use json.dumps for pretty printing
print(json.dumps(parsed, indent=4, sort_keys=True))
```

By giving an __access token__, you can get __authorized channel__ data. It requires the __channel_read__ scope. You __stream_key__ will also be available.

Success
---

```json
{
    "_id": 22747064,
    "_links": {
        "chat": "https://api.twitch.tv/kraken/chat/test_user1",
        # ... (truncated for easy reading)
        "videos": "https://api.twitch.tv/kraken/channels/test_user1/videos"
    },
    "abuse_reported": null,
    # ... (truncated for easy reading)
    "views": 356
}
```

Error
---

```json
{
    "error": "Unauthorized",
    "message": "Token invalid or missing required scope",
    "status": 401
}
```

Public Channel Data
---

```python
import pytwitch # pytwitch package
import json # only used for pretty printing

# Get public data of channel='test_user1'
parsed = pytwitch.Channels().get(channel='test_user1')
# Use json.dumps for pretty printing
print(json.dumps(parsed, indent=4, sort_keys=True))
```

By giving an __channel name__, you can get __public avaialble channel__ data. It requires the no __access token__!

Success
---

```json
{
    "_id": 22747064,
    "_links": {
        "chat": "https://api.twitch.tv/kraken/chat/test_user1",
        # ... (truncated for easy reading)
        "videos": "https://api.twitch.tv/kraken/channels/test_user1/videos"
    },
    "abuse_reported": null,
    # ... (truncated for easy reading)
    "views": 52
}
```

Error
---

```json
{
    "error": "Not Found",
    "message": "Channel 'requested channel name' does not exist",
    "status": 404
}
```
