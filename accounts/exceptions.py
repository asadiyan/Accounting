from rest_framework.exceptions import APIException


class InventoryIsNotEnoughException(APIException):
    status_code = 200  # or whatever you want
    default_code = '4026'
    #  Custom response below
    default_detail = {"code": 4026, "message": "Account balance is not enough"}
