# Python Pinterest API

### Usage

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
api.board().create("halloween", description="Fun Costumes")

# Fetch board
api.board("username/halloween").fetch()

# Fetch pins on board
api.board("username/halloween").pins()

# Edit board
api.board("username/halloween").edit(new_name="Costumes", new_description="Halloween Costume Ideas")

# Delete board
api.board("username/halloween").delete()

# Fetch board suggestions
api.suggest_boards(pin=162129655315312286)

# Fetch authenciated user's pins
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
```


### Resources

[Pinterest Developer API](https://developers.pinterest.com/docs/getting-started/introduction/)
[Pinterest API Explorer](https://developers.pinterest.com/tools/api-explorer/)
