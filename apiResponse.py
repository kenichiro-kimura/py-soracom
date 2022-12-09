import json

class ApiResponse:
    def __init__(self,status,response):
        self.status = status
        self.response = response
        self.data = None
        responseBody = self.response.decode('utf-8')
        if(self.status >= 200 and self.status < 400 and len(responseBody) > 0):
            self.data = json.loads(responseBody)
        else:
            self.data = None