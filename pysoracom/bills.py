from pysoracom.apiClient import callAPI

def getBillingHistory(api):
    return callAPI(api,url="/bills", method="GET")

def getBilling(api,yyyyMM):
    return callAPI(api,url="/bills/"+yyyyMM, method="GET")

def getBillingPerDay(api,yyyyMM):
    return callAPI(api,url="/bills/"+yyyyMM+"/daily", method="GET")

def exportBilling(api,yyyyMM,**kwargs):
    body = {
        "export_mode": kwargs.get("export_mode"),
    }
    return callAPI(api,url="/bills/"+yyyyMM+"/export", method="POST",body=body)

def getLatestBilling(api):
    return callAPI(api,url="/bills/latest", method="GET")

def exportLatestBilling(api,**kwargs):
    body = {
        "export_mode": kwargs.get("export_mode"),
    }
    return callAPI(api,url="/bills/latest/export", method="POST",body=body)