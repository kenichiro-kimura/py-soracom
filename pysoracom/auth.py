from pysoracom.apiClient import callAPI

def auth(api):
    body = {
        "email": api.authRequest.Email,
        "password": api.authRequest.Password,
        "authKeyId": api.authRequest.AuthKeyID,
        "authKey": api.authRequest.AuthKey,
        "username": api.authRequest.Username,
        "operatorId": api.authRequest.OperatiorID,
    }

    response = callAPI(api,url="/auth", method="POST",body=body)

    if(response.status == 200):
        api.token = response.data['token']
        api.apiKey = response.data['apiKey']
        api.headers['X-Soracom-API-Key'] = api.apiKey
        api.headers['X-Soracom-Token'] = api.token
        return True
    else:
        return False

def logout(api):
    callAPI(api,url="/auth/logout", method="POST")