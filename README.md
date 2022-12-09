# py-soracom

SORACOM API client library for Python

## how to use

1. set environment variable
  - SORACOM_EMAIL
  - SORACOM_PASSWORD
  - SORACOM_AUTH_KEY_ID
  - SORACOM_AUTH_KEY
  - SORACOM_USERNAME
  - SORACOM_OPERATOR_ID
  - SORACOM_COVERAGE
   
  if you use root account, you need to set SORACOM_EMAIL and SORACOM_PASSWORD.  
  if you use authKeyId, you need to set SORACOM_AUTH_KEY_ID and SORACOM_AUTH_KEY.  
  if you use SAM user, you need to set SORACOM_USERNAME and SORACOM_OPERATOR_ID and SORACOM_PASSWORD.   
  if you use global coverage, you need to set SORACOM_COVERAGE to 'g'

2. install urllib3
  ```bash
  pip install urllib3
  ```

## sample code

```python
from py-soracom.soracom import Soracom
from py-soracom.authRequest import AuthRequest
from py-soracom.auth import auth
import json
import py-soracom.sora_cam

authRequest = AuthRequest()
api = Soracom(authRequest)
auth(api)
sora_cameDevices = sora_cam.listSoraCamDevices(api).data
for i in sora_cameDevices:
    deviceId = i['deviceId']
    device = sora_cam.getSoraCamDevice(api,deviceId).data
    print(device)
```

## supported APIs

- auth
  - auth
  - logout
- sora_cam
  - listSoraCamDevices
  - getSoraCamDevice
  - getSoraCamDeviceExportUsage
  - listSoraCamDeviceImageExportsForDevice
  - exportSoraCamDeviceRecordedImage
  - getSoraCamDeviceExportedImage
  - getSoraCamDeviceStreamingVideo
  - listSoracamDeviceVideoExportsForDevice
  - exportSoraCamDeviceRecordedVideo
  - getSoraCamDeviceExportedVideo
  - listSoraCamDeviceImageExports
  - listSoraCamDeviceVideoExports
  - listSoraCamLicensePacks

possible arguments are described in https://users.soracom.io/ja-jp/tools/api/reference/

if you want to use other APIs, please add a module and send pull request, or use apiClient.callAPI method.
