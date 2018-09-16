from typing import Any, Dict, List

from .board import Board
from .me import Me
from . import oauth2
from .pin import Pin
from .user import User


class Pinterest:

    def __init__(self, token: str):
        self.token = token
        self._me = Me(self.token)

    def me(self, fields: List[str] = None) -> Dict[str, Any]:
        """Return authenticated user's information"""
        return self._me(fields=fields)

    def user(self, username: str, fields: List[str] = None) -> Dict[str, Any]:
        """Return a user's information"""
        return User(self.token, username).fetch(fields=fields)

    def board(self, name: str = None) -> Board:
        return Board(self.token, name=name)

    def pin(self, pin_id: str = None) -> Pin:
        return Pin(self.token, pin_id=pin_id)

    def __getattr__(self, attr):
        """Dispatch methods from Me() dynamically"""
        if hasattr(self._me, attr):
            def wrapper(*args, **kwargs):
                return getattr(self._me, attr)(*args, **kwargs)
            return wrapper
