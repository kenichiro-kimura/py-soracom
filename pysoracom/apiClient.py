from pysoracom.apiResponse import ApiResponse
import json

def callAPI(self, **kwargs):
    if not ('url' in kwargs and 'method' in kwargs):
        raise Exception("Invalid arguments")
    if not ('body' in kwargs):
        kwargs['body'] = ""
    url = kwargs['url']
    method = kwargs['method']
    body = kwargs['body']

    apiUrl = self.baseURL + url
    if (method == "GET"):
        response = self.http.request(method, apiUrl, headers=self.headers)
    elif (method == "POST"):
        response = self.http.request(
            method, apiUrl, headers=self.headers, body=json.dumps(body))
    else:
        raise Exception("Invalid method")

    return ApiResponse(response.status, response.data)

def kwargsToArgs(self, kwargs):
    args = ""
    for key in kwargs:
        if (args != ""):
            args += "&"
        args += key + "=" + kwargs[key]

    if (args != ""):
        args = "?" + args
    return args
