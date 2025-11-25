from abc import ABC, abstractmethod

class Earning(ABC):
    @abstractmethod
    def get_Earning(self) -> float:
        pass