from pysoracom.apiClient import *

def listSoraCamDevices(api):
    return callAPI(api,url="/sora_cam/devices", method="GET")

def getSoraCamDevice(api,deviceID):
    return callAPI(api,url="/sora_cam/devices/" + deviceID, method="GET")

def getSoraCamDeviceExportUsage(api,deviceID):
    return callAPI(api,url="/sora_cam/devices/" + deviceID + "/exports/usage", method="GET")

def listSoraCamDeviceImageExportsForDevice(api,deviceID,**kwargs):
    url = "/sora_cam/devices/" + deviceID + "/images/exports" + kwargsToArgs(kwargs)
    return callAPI(api,url=url, method="GET")

def exportSoraCamDeviceRecordedImage(api,deviceID,time):
    body = {
        "time": time
    }
    return callAPI(api,url="/sora_cam/devices/" + deviceID + "/images/exports", method="POST",body=body)

def getSoraCamDeviceExportedImage(api,deviceID,exportID):
    return callAPI(api,url="/sora_cam/devices/" + deviceID + "/images/exports/" + exportID, method="GET")

def getSoraCamDeviceStreamingVideo(api,deviceID,**kwargs):
    url = "/sora_cam/devices/" + deviceID + "/stream" + kwargsToArgs(kwargs)
    return callAPI(api,url=url, method="GET")

def listSoracamDeviceVideoExportsForDevice(api,deviceID,**kwargs):
    url = "/sora_cam/devices/" + deviceID + "/videos/exports" + kwargsToArgs(kwargs)
    return callAPI(api,url=url, method="GET")

def exportSoraCamDeviceRecordedVideo(api,deviceID,fromTime,toTime):
    body = {
        "from": fromTime,
        "to": toTime
    }
    return callAPI(api,url="/sora_cam/devices/" + deviceID + "/videos/exports", method="POST",body=body)

def getSoraCamDeviceExportedVideo(api,deviceID,exportID):
    return callAPI(api,url="/sora_cam/devices/" + deviceID + "/videos/exports/" + exportID, method="GET")

def listSoraCamDeviceImageExports(api,**kwargs):
    url = "/sora_cam/devices/images/exports" + kwargsToArgs(kwargs)
    return callAPI(api,url=url, method="GET")
    
def listSoraCamDeviceVideoExports(api,**kwargs):
    url = "/sora_cam/devices/videos/exports" + kwargsToArgs(kwargs)
    return callAPI(api,url=url, method="GET")

def listSoraCamLicensePacks(api):
    return callAPI(api,url="/sora_cam/license_packs", method="GET")

def updateSoraCamLicensePackQuantity(api,licensePackID,currentQuantity,desiredQuantity):
    body = {
        "currentQuantity": currentQuantity,
        "desiredQuantity": desiredQuantity,
    }
    return callAPI(api,url="/sora_cam/license_packs/" + licensePackID + "/quantity", method="PUT",body=body)