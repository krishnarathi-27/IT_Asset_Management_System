from dataclasses import dataclass

@dataclass
class MyBaseException(Exception):
    error_code : int
    error_message : str
    error_description : str

class CustomException(MyBaseException):
    pass

class DBException(MyBaseException):
    pass

class InvalidCredentials(MyBaseException):
    pass

class DataNotExists(MyBaseException):
    pass

class DataAlreadyExists(MyBaseException):
    pass
