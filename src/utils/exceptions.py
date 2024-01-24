class InvalidUserCredentials(Exception):
    pass

class DataAlreadyExists(Exception):
    pass

class UserAlreadyExistsException(DataAlreadyExists):
    pass

class VendorAlreadyExists(DataAlreadyExists):
    pass

class CategoryAlreadyExists(DataAlreadyExists):
    pass

class DBException(Exception):
    pass

class NoDataExistsException(Exception):
    pass
