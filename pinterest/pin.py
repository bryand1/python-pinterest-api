import os
from typing import Dict, List

from . import config
from .err import PinterestException
from .util import pinterest_request


class Pin:

    def __init__(self, token: str, pin_id: str = None):
        self.token = token
        self.pin_id = pin_id

    def create(self, board: str, note: str, link: str = None,
               image: str = None, image_url: str = None, image_base64: str = None,
               fields: List[str] = None) -> Dict:
        """
        Creates a Pin for the authenticated user.
        The default response returns the note, URL, link and ID of the created Pin.

        board (required): The board you want the new Pin to be on. In the format <username>/<board_name>.
        note (required): The Pin’s description.
        link (optional): The URL the Pin will link to when you click through.

        And one of the following three options is required:
        image: Upload the image you want to pin using multipart form data.
        image_url: The link to the image that you want to Pin.
        image_base64: The link of a Base64 encoded image.

        fields: attribution, board, color, counts, created_at, creator,
                id, image, link, media, metadata, note, original_link, url

        POST /v1/pins/
        """
        if fields is None:
            fields = ['note', 'url', 'link', 'id']
        url = config.api_url + '/v1/pins/'
        params = {'access_token': self.token, 'fields': ','.join(fields)}
        data = {
            'board': board,
            'note': note,
            'link': link
        }
        files = {}
        if image is not None:
            if not os.path.exists(image):
                raise PinterestException("Pin: image does not exist")
            files['image'] = open(image, 'rb')
        elif image_url is not None:
            data['image_url'] = image_url
        elif image_base64 is not None:
            data['image_base64'] = image_base64
        else:
            raise PinterestException("Pin: create() requires either image, image_url, or image_base64")
        return pinterest_request('post', url, params=params, data=data, files=files)

    def fetch(self, fields: List[str] = None) -> Dict:
        """
        The default response returns the ID, link, URL and note of the Pin.

        fields: attribution, board, color, counts, created_at, creator,
                id, image, link, media, metadata, note, original_link, url

        GET /v1/pins/<pin>/
        """
        if fields is None:
            fields = ['id', 'link', 'url', 'note']
        url = config.api_url + '/v1/pins/{pin_id}/'.format(pin_id=self.pin_id)
        params = {'access_token': self.token, 'fields': ','.join(fields)}
        return pinterest_request('get', url, params=params)

    def edit(self, board: str = None, note: str = None, link: str = None, fields: List[str] = None) -> Dict:
        """
        Changes the board, description and/or link of the Pin.

        pin (required): The ID (unique string of numbers and letters) of the Pin you want to edit.
        board (optional): The board you want to move the Pin to, in the format <username>/<board_name>.
        note (optional): The new Pin description.
        link (optional): The new Pin link. Note: You can only edit the link of a repinned Pin if
                         the pinner owns the domain of the Pin in question, or if the Pin itself
                         has been created by the pinner.

        fields: attribution, board, color, counts, created_at, creator,
                id, image, link, media, metadata, note, original_link, url

        PATCH /v1/pins/<pin>/
        """
        if board is None and note is None and link is None:
            raise PinterestException("Pin: edit() requires valid board, note, or link")
        if fields is None:
            fields = ['id', 'link', 'url', 'note']
        url = config.api_url + '/v1/pins/{pin_id}/'.format(pin_id=self.pin_id)
        params = {'access_token': self.token, 'fields': ','.join(fields)}
        data = {}
        if board is not None:
            data['board'] = board
        if note is not None:
            data['note'] = note
        if link is not None:
            data['link'] = link
        return pinterest_request('patch', url, params=params, data=data)

    def delete(self) -> Dict:
        """
        Deletes the specified Pin. This action is permanent and cannot be undone.

        DELETE /v1/pins/<pin>/
        """
        url = config.api_url + '/v1/pins/{pin_id}/'.format(pin_id=self.pin_id)
        params = {'access_token': self.token}
        return pinterest_request('delete', url, params=params)
