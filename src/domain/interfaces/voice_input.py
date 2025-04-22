from abc import ABC, abstractmethod

class VoiceInputInterface(ABC):
    @abstractmethod
    def listen(self) -> str:
        pass
