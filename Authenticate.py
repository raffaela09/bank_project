from abc import ABC, abstractmethod

class Authenticate(ABC):
    
    @abstractmethod
    def login(self, password: str):
        pass    

    @abstractmethod
    def require_login(self):
        pass
    
    @abstractmethod
    def logout(self) -> bool:
        pass

        
