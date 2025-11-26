from abc import ABC, abstractmethod

class Authenticate(ABC):
    
    @abstractmethod
    def auntheticate(self, password: str) -> bool:
        pass
    

        
