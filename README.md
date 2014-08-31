PyTwitch 0.0.2
===

No stable realease yet, however, I'll document my progress here. Until a stable release is ready.

Install
===

You can install pytwitch with pip. Just remember it's __far from done yet__. So there isn't much you can do with it... yet!

```bash
pip install pytwitch
```

Channels
===

__Index__

- [Get Authorized Channel Data](#Get Authorized Channel Data)
- [Get Public Channel Data](#Get Public Channel Data)
- [Set Game/Title of Stream](#Set Game/Title of Stream)

Get Authorized Channel Data
---

```python
import pytwitch # pytwitch package
import json # only used for pretty printing

token = 'Your Access Token'

parsed = pytwitch.Channels().get(token=token)
# Use json.dumps for pretty printing
print(json.dumps(parsed, indent=4, sort_keys=True))
```

By giving an __access token__, you can get __authorized channel__ data.
It requires the __channel_read__ scope!
Your __stream_key__ will also be available.

Success
---

```json
{
    "_id": 22747064,
    "_links": {
        "chat": "https://api.twitch.tv/kraken/chat/test_user1",
        ...
        "videos": "https://api.twitch.tv/kraken/channels/test_user1/videos"
    },
    "abuse_reported": null,
    ...
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

Get Public Channel Data
---

```python
import pytwitch # pytwitch package
import json # only used for pretty printing

# Get public data of channel='test_user1'
parsed = pytwitch.Channels().get(channel='test_user1')
# Use json.dumps for pretty printing
print(json.dumps(parsed, indent=4, sort_keys=True))
```

By giving an __channel='name'__, you can get __public available channel__ data.

Success
---

```json
{
    "_id": 22747064,
    "_links": {
        "chat": "https://api.twitch.tv/kraken/chat/test_user1",
        ...
        "videos": "https://api.twitch.tv/kraken/channels/test_user1/videos"
    },
    "abuse_reported": null,
    ...
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

Set Game/Title of Stream
---

```python
import pytwitch # pytwitch package
import json # only used for pretty printing

token = 'Your Access Token'
parsed = pytwitch.Channels().set(token=token, status='Custom Title', game="Game")
print(json.dumps(parsed, indent=4, sort_keys=True))
```

By giving an __access token__, you can set __authorized channel__ data.
Only __status__ (read title) and __game__ can be set, limit by __Twitch API__.
It requires the __channel_editor__ scope!

If __token__ isn't set, it will return with a error:

```
'Error: Access token (token) wasn\'t set.'
```

If __status__ isn't set or __game__ (or both) isn't set in the call, those __won't be changed__.
Data returned will be a __JSON object__ of channel data. (__stream_key__ not included, see get method for getting the __stream_key__)

Success
---

```json
{
    "_id": 22747064,
    "_links": {
        "chat": "https://api.twitch.tv/kraken/chat/test_user1",
        ...
        "videos": "https://api.twitch.tv/kraken/channels/dhhtv/test_user1"
    },
    "background": null,
    "game": "Game",
    ...
    "status": "Custom Title",
    "video_banner": "http://static-cdn.jtvnw.net/jtv_user_pictures/dhhtv-channel_offline_image-c7687423fa9f7b40-640x360.jpeg"
}
```
