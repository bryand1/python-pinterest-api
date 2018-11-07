from typing import Dict

from . import config
from .err import PinterestException
from .util import pinterest_request


class Section:

    def __init__(self, token, board: str, identifier: str = None):
        self.token = token
        self.board = board
        self.identifier = identifier

    def create(self) -> Dict:
        """
        Creates a section for the authenticated user. The default response returns the ID of the created section.

        PUT /v1/board/<board>/sections/
        """
        if self.identifier is None:
            raise PinterestException("Section: create() requires valid section title")
        url = config.api_url + '/v1/board/{board}/sections/'.format(board=self.board)
        params = {'access_token': self.token}
        data = {'title': self.identifier}
        return pinterest_request('put', url, params=params, data=data)

    def pins(self) -> Dict:
        """
        Gets the pins for a board section.

        GET /v1/board/sections/<section_spec:section>/pins/
        """
        if self.identifier is None:
            raise PinterestException("Section: pins() requires valid section identifier")
        url = config.api_url + '/v1/board/sections/{identifier}/pins/'.format(identifier=self.identifier)
        params = {'access_token': self.token}
        return pinterest_request('put', url, params=params)

    def delete(self) -> Dict:
        """
        Deletes a board section

        <section> identifier should be a string of integers (e.g. "4989415010584246390")

        DELETE /v1/board/sections/<section>/
        """
        if self.identifier is None:
            raise PinterestException("Section: delete() requires valid section identifier")
        url = config.api_url + '/v1/board/sections/{identifier}/'.format(identifier=self.identifier)
        params = {'access_token': self.token}
        return pinterest_request('delete', url, params=params)
