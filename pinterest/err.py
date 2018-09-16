class PinterestException(Exception):
    """"""


class PinterestHttpException(PinterestException):

    def __init__(self, code, message):
        super().__init__()
        self.code = code
        self.message = message

    def __str__(self):
        return "PinterestHttpException: [{code}] {message}".format(code=self.code, message=self.message)

    def __repr__(self):
        return "<PinterestHttpException [{code}]>".format(code=self.code)
