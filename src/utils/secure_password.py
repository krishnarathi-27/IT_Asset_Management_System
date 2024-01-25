import hashlib
from abc import ABC, abstractmethod

class SecurePassword(ABC):
    
    @abstractmethod
    def secure_password(self,password: str) -> str:
        pass

class HashPassword(SecurePassword):

    def secure_password(self,password: str) -> str:
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return hashed_password
    