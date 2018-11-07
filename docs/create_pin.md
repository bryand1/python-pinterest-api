# Create Pin


Pinterest allows three different ways to post images:   
1. **image** - file handle to image on local filesystem
2. **image_url**
3. **image_base64** - base64 encoded string


### Usage

```python
import base64
import pinterest

api = pinterest.Pinterest(token="ApFF9WBrjug_xhJPsETri2jp9pxgFVQfZNayykxFOjJQhWAw")

# Create pin using image on local filesystem
api.pin().create(
    'bryand1/technology',     # <username/board>
    'Git data structures',    # note
    'https://github.com',     # the pin will link to this url
    image='./images/git.png'  # available on local filesystem
)

# Create pin using image url
api.pin().create(
    'bryand1/technology',    # <username/board>
    'Git data structures',   # note
    'https://github.com',    # the pin will link to this url
    image_url='https://s3.amazonaws.com/bryand1/images/git.png'
)

# Create pin using base64 encoded image
with open('./images/git.png', 'rb') as fh:
    image_base64 = base64.b64encode(fh.read()).decode()
api.pin().create(
    'bryand1/technology',   # <username/board>
    'Git data structures',  # note
    'https://github.com',   # the pin will link to this url  
    image_base64=image_base64
)

```


### Response

```javascript
{
  "data": {
    "id": "695665473666621315",
    "link": "https://www.pinterest.com/r/pin/695665473666621315/4989327273560649264/a248f805acfbde23a36cbc0a6cbbb7cfa5377fcb8f5e647a9104801c75e99cbb",
    "note": "Git data structures",
    "url": "https://www.pinterest.com/pin/695665473666621315/"
  },
  "ratelimit": {
      "limit": 10,
      "remaining": 9
  }
}

```


### Resources

[Pinterest API - Pins](https://developers.pinterest.com/docs/api/pins/)  
[Base64](https://en.wikipedia.org/wiki/Base64)  
