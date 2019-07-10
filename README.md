# Python Pinterest API

![license MIT](https://s3-us-west-1.amazonaws.com/bryand1/images/badges/license-MIT-blue.svg)
![python 3.6 | 3.7](https://s3-us-west-1.amazonaws.com/bryand1/images/badges/python-3.6-3.7.svg)


## Getting Started

```bash
pip install pinterest-api
```


## Usage

```python
import pinterest

# Generate OAuth2 authorization link
link = pinterest.oauth2.authorization_url(app_id, redirect_uri)

# Initialize API by passing OAuth2 token
api = pinterest.Pinterest(token="ApFF9WBrjug_xhJPsETri2jp9pxgFVQfZNayykxFOjJQhWAw")

# Fetch authenticated user's data
api.me()

# Fetch authenticated user's boards
api.boards()

# Create board
api.board().create("Halloween", description="Fun Costumes")

# Fetch board
api.board("695665542379607495").fetch()
api.board("username/halloween").fetch()

# Fetch pins on board
api.board("username/halloween").pins()

# Edit board
api.board("username/halloween").edit(new_name="Costumes", new_description="Halloween Costume Ideas")

# Delete board
api.board("username/halloween").delete()

# Fetch board suggestions
api.suggest_boards(pin=162129655315312286)

# Fetch authenticated user's pins
api.pins()

# Create a pin
api.pin().create(board, note, link, image_url=image_url)

# Fetch a pin
api.pin(162129655315312286).fetch()

# Edit a pin
api.pin(162129655315312286).edit(board, note, link)

# Delete a pin
api.pin(162129655315312286).delete()

# Search boards (Optional cursor)
api.search_boards(query, cursor=None)

# Search pins (Optional cursor)
api.search_pins(query, cursor=None)

# Follow a board
api.follow_board(board)

# Follow a user
api.follow_user(username)

# Return the users who follow the authenticated user
api.followers(cursor=None)

# Return the boards that the authenticated user follows
api.following_boards(cursor=None)

# Return the topics the authenticated user follows
api.following_interests(cursor=None)

# Return the users the authenticated user follows
api.following_users(cursor=None)

# Unfollow board
api.unfollow_board(board)

# Make authenticated user unfollow user
api.unfollow_user(username)

# Fetch another user's info
api.user(username)

# Fetch board sections
api.board("695665542379586148").sections()

# Create board section
api.board("695665542379586148").section("Section Title").create()

# Delete board section
api.board("695665542379586148").section("4989415010584246390").delete()

# Fetch pins in board section
api.board("695665542379586148").section("4989343507360527350").pins()
```


## Responses

The Pinterest API responses are in JSON format.

```python
api.me()  # By default, retry http request up to 3 times
```

```javascript
{
  "data": {
    "first_name": "Bryan",
    "id": "695665611098925391",
    "last_name": "Andrade",
    "url': "https://www.pinterest.com/bandrade1815/"
  },
  "ratelimit": {
      "limit": 10,
      "remaining": 9
  }
}
```


## Resources

[Pinterest Developer API](https://developers.pinterest.com/docs/getting-started/introduction/)  
[Pinterest API Explorer](https://developers.pinterest.com/tools/api-explorer/)
