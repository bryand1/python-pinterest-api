from typing import List

from . import config
from .err import PinterestException
from .section import Section
from .util import do_request


class Board:

    def __init__(self, token: str, identifier: str = None):
        """identifier uses board:spec format '<username>/<board_name>' or string of integers 695665542379586148"""
        self.token = token
        self.identifier = identifier

    def create(self, name: str, description: str = None, fields: List[str] = None):
        """
        Creates a board for the authenticated user.

        The default response returns the ID, URL and name of the created board.

        fields: counts, created_at, creator, description, id, image, name, privacy, reason, url

        POST/v1/boards/
        """
        if fields is None:
            fields = ['name', 'id', 'url']
        url = config.api_url + "/v1/boards/"
        params = {
            'access_token': self.token,
            'fields': ','.join(fields)
        }
        data = {
            "name": name,
            "description": description,
        }
        return do_request('post', url, params=params, data=data).json()

    def fetch(self, fields: List[str] = None):
        """
        The default response returns the ID, URL and name of the specified board.

        GET /v1/boards/<board>/
        """
        if fields is None:
            fields = ['id', 'url', 'name']
        url = config.api_url + "/v1/boards/{identifier}/".format(identifier=self.identifier)
        params = {'access_token': self.token, 'fields': ','.join(fields)}
        return do_request('get', url, params=params).json()

    def pins(self, cursor: str = None, fields: List[str] = None):
        """The default response returns a list of ordered Pins on the board with their ID, URL, link and description.

        Pins are ordered from most recently created to least recent.

        fields: attribution, board, color, counts, created_at, creator, id,
                image, link, media, metadata, note, original_link, url

        GET /v1/boards/<board>/pins/
        """
        if fields is None:
            fields = ['id', 'url', 'link', 'description']
        url = config.api_url + "/v1/boards/{identifier}/pins/".format(identifier=self.identifier)
        params = {'access_token': self.token, 'fields': ','.join(fields)}
        if cursor is not None:
            params['cursor'] = cursor
        return do_request('get', url, params=params).json()

    def edit(self, new_name: str = None, new_description: str = None, fields: List[str] = None):
        """Changes the chosen board’s name and/or description.

        The default response returns the ID, URL and name of the edited board.

        fields: counts, created_at, creator, description, id, image, name, privacy, reason, url

        PATCH /v1/boards/<board>/
        """
        if new_name is None and new_description is None:
            raise PinterestException("Board: edit() requires valid name or description")
        if fields is None:
            fields = ['id', 'name', 'url']
        url = config.api_url + '/v1/boards/{identifier}/'.format(identifier=self.identifier)
        params = {'access_token': self.token, 'fields': ','.join(fields)}
        data = {"name": new_name, "description": new_description}
        return do_request('patch', url, params=params, data=data).json()

    def delete(self):
        """
        Deletes the specified board. This action is permanent and cannot be undone.

        DELETE /v1/boards/<board>/
        """
        if self.identifier is None:
            raise PinterestException("Board: delete() requires valid identifier")
        url = config.api_url + "/v1/boards/{identifier}/".format(identifier=self.identifier)
        params = {'access_token': self.token}
        return do_request('delete', url, params=params).json()

    def sections(self, cursor: str = None):
        """
        Gets sections for a board.

        GET /v1/board/<board>/sections/
        """
        if self.identifier is None:
            raise PinterestException("Board: sections() requires valid identifier")
        url = config.api_url + '/v1/board/{identifier}/sections/'.format(identifier=self.identifier)
        params = {'access_token': self.token}
        if cursor is not None:
            params['cursor'] = cursor
        return do_request('get', url, params=params).json()

    def section(self, identifier: str = None) -> Section:
        return Section(self.token, self.identifier, identifier=identifier)
