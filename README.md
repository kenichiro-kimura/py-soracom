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

2. install urllib3
  ```bash
  pip install urllib3
  ```

## sample code

```python
from py-soracom.soracom import Soracom
from py-soracom.authRequest import AuthRequest
import json

authRequest = AuthRequest()
api = Soracom(authRequest)
api.auth()
sora_cameDevices = api.listSoraCamDevices().data
for i in sora_cameDevices:
    deviceId = i['deviceId']
    device = api.getSoraCamDevice(deviceId).data
    print(device)
```

## supported APIs

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

if you want to use other APIs, please add method to soracom.py and send pull request, or use callAPI method.
