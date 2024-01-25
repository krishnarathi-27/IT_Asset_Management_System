class InvalidUserCredentials(Exception):
    pass

class DataAlreadyExists(Exception):
    pass

class UserAlreadyExistsException(DataAlreadyExists):
    pass

class VendorAlreadyExistsException(DataAlreadyExists):
    pass

class CategoryAlreadyExistsException(DataAlreadyExists):
    pass

class DBException(Exception):
    pass

class NoDataExistsException(Exception):
    pass

class PasswordsNotMatchException(Exception):
    pass

class VendorNotExistsException(Exception):
    pass