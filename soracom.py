import urllib3
import json
from apiResponse import ApiResponse

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
            self.logout()

    def auth(self):
        body = {
            "email": self.authRequest.Email,
            "password": self.authRequest.Password,
            "authKeyId": self.authRequest.AuthKeyID,
            "authKey": self.authRequest.AuthKey,
            "username": self.authRequest.Username,
            "operatorId": self.authRequest.OperatiorID,
        }

        response = self.callAPI(url="/auth", method="POST",body=body)

        if(response.status == 200):
            self.token = response.data['token']
            self.apiKey = response.data['apiKey']
            self.headers['X-Soracom-API-Key'] = self.apiKey
            self.headers['X-Soracom-Token'] = self.token
            return True
        else:
            return False

    def logout(self):
        self.callAPI(url="/auth/logout", method="POST")

    def listSoraCamDevices(self):
        return self.callAPI(url="/sora_cam/devices", method="GET")

    def getSoraCamDevice(self,deviceID):
        return self.callAPI(url="/sora_cam/devices/" + deviceID, method="GET")

    def getSoraCamDeviceExportUsage(self,deviceID):
        return self.callAPI(url="/sora_cam/devices/" + deviceID + "/exports/usage", method="GET")

    def listSoraCamDeviceImageExportsForDevice(self,deviceID,**kwargs):
        url = "/sora_cam/devices/" + deviceID + "/images/exports" + self.kwargsToArgs(kwargs)
        return self.callAPI(url=url, method="GET")

    def exportSoraCamDeviceRecordedImage(self,deviceID,time):
        body = {
            "time": time
        }
        return self.callAPI(url="/sora_cam/devices/" + deviceID + "/images/exports", method="POST",body=body)

    def getSoraCamDeviceExportedImage(self,deviceID,exportID):
        return self.callAPI(url="/sora_cam/devices/" + deviceID + "/images/exports/" + exportID, method="GET")

    def getSoraCamDeviceStreamingVideo(self,deviceID,**kwargs):
        url = "/sora_cam/devices/" + deviceID + "/stream" + self.kwargsToArgs(kwargs)
        return self.callAPI(url=url, method="GET")

    def listSoracamDeviceVideoExportsForDevice(self,deviceID,**kwargs):
        url = "/sora_cam/devices/" + deviceID + "/videos/exports" + self.kwargsToArgs(kwargs)
        return self.callAPI(url=url, method="GET")

    def exportSoraCamDeviceRecordedVideo(self,deviceID,fromTime,toTime):
        body = {
            "from": fromTime,
            "to": toTime
        }
        return self.callAPI(url="/sora_cam/devices/" + deviceID + "/videos/exports", method="POST",body=body)

    def getSoraCamDeviceExportedVideo(self,deviceID,exportID):
        return self.callAPI(url="/sora_cam/devices/" + deviceID + "/videos/exports/" + exportID, method="GET")

    def listSoraCamDeviceImageExports(self,**kwargs):
        url = "/sora_cam/devices/images/exports" + self.kwargsToArgs(kwargs)
        return self.callAPI(url=url, method="GET")
        
    def listSoraCamDeviceVideoExports(self,**kwargs):
        url = "/sora_cam/devices/videos/exports" + self.kwargsToArgs(kwargs)
        return self.callAPI(url=url, method="GET")

    def listSoraCamLicensePacks(self):
        return self.callAPI(url="/sora_cam/license_packs", method="GET")

    def updateSoraCamLicensePackQuantity(self,licensePackID,currentQuantity,desiredQuantity):
        body = {
            "currentQuantity": currentQuantity,
            "desiredQuantity": desiredQuantity,
        }
        return self.callAPI(url="/sora_cam/license_packs/" + licensePackID + "/quantity", method="PUT",body=body)

    def callAPI(self,**kwargs):
        if not ('url' in kwargs and 'method' in kwargs):
            raise Exception("Invalid arguments")
        if not ('body' in kwargs):
            kwargs['body'] = ""
        url = kwargs['url']
        method = kwargs['method']
        body = kwargs['body']

        apiUrl = self.baseURL + url
        if(method == "GET"):
            response = self.http.request(method, apiUrl, headers=self.headers)
        elif (method == "POST"):
            response = self.http.request(method, apiUrl, headers=self.headers, body=json.dumps(body))
        else:
            raise Exception("Invalid method")

        return ApiResponse(response.status, response.data)

    def kwargsToArgs(self,kwargs):        
        args = ""
        for key in kwargs:
            if(args != ""):
                args += "&"
            args += key + "=" + kwargs[key]        

        if(args != ""):
            args = "?" + args
        return args
