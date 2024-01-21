from abc import ABC, abstractmethod

class GeradorImageStrategy(ABC):
    @abstractmethod
    def processar_imagem(self, imagem):
        pass
