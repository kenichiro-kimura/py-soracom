from pysoracom.apiResponse import ApiResponse
import json

def callAPI(api, **kwargs):
    if not ('url' in kwargs and 'method' in kwargs):
        raise Exception("Invalid arguments")
    if not ('body' in kwargs):
        kwargs['body'] = ""
    url = kwargs['url']
    method = kwargs['method']
    body = kwargs['body']

    apiUrl = api.baseURL + url
    if (method == "GET"):
        response = api.http.request(method, apiUrl, headers=api.headers)
    elif (method == "POST"):
        response = api.http.request(
            method, apiUrl, headers=api.headers, body=json.dumps(body))
    else:
        raise Exception("Invalid method")

    return ApiResponse(response.status, response.data)

def kwargsToArgs(kwargs):
    args = ""
    for key in kwargs:
        if (args != ""):
            args += "&"
        args += key + "=" + kwargs[key]

    if (args != ""):
        args = "?" + args
    return args
