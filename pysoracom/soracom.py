import urllib3
import json
from pysoracom.auth import logout

class Soracom:
    baseURL = "https://api.soracom.io/v1"
    headers = {
        'Content-Type': 'application/json',
    }
    token = None
    apiKey = None

    def __init__(self,authRequest):
        if(authRequest.Coverage == "g"):
            self.baseURL = "https://g.api.soracom.io/v1"
        self.http = urllib3.PoolManager()
        self.authRequest = authRequest

    def __del__(self):
        if(self.token is not None):
            logout(self)
