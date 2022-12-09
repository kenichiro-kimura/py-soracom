from pysoracom.apiClient import callAPI

def listSoraCamDevices(self):
    return callAPI(self,url="/sora_cam/devices", method="GET")

def getSoraCamDevice(self,deviceID):
    return callAPI(self,url="/sora_cam/devices/" + deviceID, method="GET")

def getSoraCamDeviceExportUsage(self,deviceID):
    return callAPI(self,url="/sora_cam/devices/" + deviceID + "/exports/usage", method="GET")

def listSoraCamDeviceImageExportsForDevice(self,deviceID,**kwargs):
    url = "/sora_cam/devices/" + deviceID + "/images/exports" + apiClient.kwargsToArgs(kwargs)
    return callAPI(self,url=url, method="GET")

def exportSoraCamDeviceRecordedImage(self,deviceID,time):
    body = {
        "time": time
    }
    return callAPI(self,url="/sora_cam/devices/" + deviceID + "/images/exports", method="POST",body=body)

def getSoraCamDeviceExportedImage(self,deviceID,exportID):
    return callAPI(self,url="/sora_cam/devices/" + deviceID + "/images/exports/" + exportID, method="GET")

def getSoraCamDeviceStreamingVideo(self,deviceID,**kwargs):
    url = "/sora_cam/devices/" + deviceID + "/stream" + apiClient.kwargsToArgs(kwargs)
    return callAPI(self,url=url, method="GET")

def listSoracamDeviceVideoExportsForDevice(self,deviceID,**kwargs):
    url = "/sora_cam/devices/" + deviceID + "/videos/exports" + apiClient.kwargsToArgs(kwargs)
    return callAPI(self,url=url, method="GET")

def exportSoraCamDeviceRecordedVideo(self,deviceID,fromTime,toTime):
    body = {
        "from": fromTime,
        "to": toTime
    }
    return callAPI(self,url="/sora_cam/devices/" + deviceID + "/videos/exports", method="POST",body=body)

def getSoraCamDeviceExportedVideo(self,deviceID,exportID):
    return callAPI(self,url="/sora_cam/devices/" + deviceID + "/videos/exports/" + exportID, method="GET")

def listSoraCamDeviceImageExports(self,**kwargs):
    url = "/sora_cam/devices/images/exports" + apiClient.kwargsToArgs(kwargs)
    return callAPI(self,url=url, method="GET")
    
def listSoraCamDeviceVideoExports(self,**kwargs):
    url = "/sora_cam/devices/videos/exports" + apiClient.kwargsToArgs(kwargs)
    return callAPI(self,url=url, method="GET")

def listSoraCamLicensePacks(self):
    return callAPI(self,url="/sora_cam/license_packs", method="GET")

def updateSoraCamLicensePackQuantity(self,licensePackID,currentQuantity,desiredQuantity):
    body = {
        "currentQuantity": currentQuantity,
        "desiredQuantity": desiredQuantity,
    }
    return callAPI(self,url="/sora_cam/license_packs/" + licensePackID + "/quantity", method="PUT",body=body)