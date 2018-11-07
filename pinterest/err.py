class PinterestException(Exception):
    """"""


class PinterestHttpException(PinterestException):

    def __init__(self, code, url, message: str = None):
        super().__init__()
        self.code = code
        self.url = url
        self.message = message or ' '

    def __str__(self):
        return "PinterestHttpException: [{code}] {url} {message}".format(
            code=self.code, url=self.url, message=self.message)

    def __repr__(self):
        return "<PinterestHttpException [{code}]>".format(code=self.code)
