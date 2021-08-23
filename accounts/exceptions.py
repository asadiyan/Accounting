from rest_framework.exceptions import APIException


class OperationImpossibleException(APIException):
    status_code = 200  # or whatever you want
    default_code = '4026'
    #  Custom response below
    default_detail = {"code": 4026, "message": "Operation is impossible! source and destination is same!"}


class AccountBalanceIsNotEnoughException(APIException):
    status_code = 200  # or whatever you want
    default_code = '4026'
    #  Custom response below
    default_detail = {"code": 4026, "message": "Account balance is not enough"}


class AccountDoesNotExist(APIException):
    status_code = 200  # or whatever you want
    default_code = '4026'
    #  Custom response below
    default_detail = {"code": 4026, "message": "Account does not exist"}
