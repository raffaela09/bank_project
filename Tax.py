from abc import ABC, abstractmethod

class Tax(ABC):
    @abstractmethod
    def get_tax_value(self) -> float:
        pass