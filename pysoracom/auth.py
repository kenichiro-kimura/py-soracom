from pysoracom.apiClient import callAPI

def auth(self):
    body = {
        "email": self.authRequest.Email,
        "password": self.authRequest.Password,
        "authKeyId": self.authRequest.AuthKeyID,
        "authKey": self.authRequest.AuthKey,
        "username": self.authRequest.Username,
        "operatorId": self.authRequest.OperatiorID,
    }

    response = callAPI(self,url="/auth", method="POST",body=body)

    if(response.status == 200):
        self.token = response.data['token']
        self.apiKey = response.data['apiKey']
        self.headers['X-Soracom-API-Key'] = self.apiKey
        self.headers['X-Soracom-Token'] = self.token
        return True
    else:
        return False

def logout(self):
    callAPI(self,url="/auth/logout", method="POST")