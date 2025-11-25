from abc import ABC, abstractmethod

class Authenticate(ABC):
    
    @abstractmethod
    def auntheticate(self, password: str) -> bool:
        pass
    
class Tax(ABC):
    @abstractmethod
    def get_tax_value(self) -> float:
        pass
        
class Earning(ABC):
    @abstractmethod
    def get_Earning(self) -> float:
        pass