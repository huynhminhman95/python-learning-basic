# Abstraction - tinh truu truong
from abc import ABC, abstractmethod

# lop truu tuong
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
 