from abc import ABC, abstractmethod

class HandDetector(ABC):
    @abstractmethod
    def detect_hand(self, image):
        pass
