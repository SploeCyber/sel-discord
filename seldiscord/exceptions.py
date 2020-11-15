from selrequests import Response

class EndpointError(Exception):
    code: int
    message: str
    response: Response

    def __init__(self, code: int, message: str,
                 response: Response=None):
        self.code = code
        self.message = message
        self.response = response