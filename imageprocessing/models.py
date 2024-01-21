from django.db import models
from .interfaces import GeradorImageStrategy
from .strategies import FotogrametriaStrategy, SegmentacaoStrategy

class ImageStrategy(models.Model):
    fotogrametria_strategy = FotogrametriaStrategy()
    segmentacao_strategy = SegmentacaoStrategy()

    def escolher_strategy(self, tipo):
        if tipo == 'fotogrametria':
            return self.fotogrametria_strategy
        elif tipo == 'segmentacao':
            return self.segmentacao_strategy
        else:
            raise ValueError("Tipo de estratégia desconhecido")

    def processar_imagem(self, imagem, tipo):
        strategy = self.escolher_strategy(tipo)
        return strategy.processar_imagem(imagem)

