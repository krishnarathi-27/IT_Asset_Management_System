from dataclasses import dataclass

@dataclass
class ApplicationException(Exception):
    error_code : int
    error_message : str
    error_description : str

@dataclass
class DBException(Exception):
    error_code : int
    error_message : str
    error_description : str
