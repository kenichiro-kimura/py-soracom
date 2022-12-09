import os

class AuthRequest:
    def __init__(self):
        self.Email = os.environ.get("SORACOM_EMAIL")
        self.Password = os.environ.get("SORACOM_PASSWORD")
        self.AuthKeyID = os.environ.get("SORACOM_AUTH_KEY_ID")
        self.AuthKey = os.environ.get("SORACOM_AUTH_KEY")
        self.Username = os.environ.get ("SORACOM_USERNAME")
        self.OperatiorID = os.environ.get("SORACOM_OPERATOR_ID")
        self.Coverage = os.environ.get("SORACOM_COVERAGE")
