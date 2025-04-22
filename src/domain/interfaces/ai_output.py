from abc import ABC, abstractmethod

class AIOutputInterface(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        pass
