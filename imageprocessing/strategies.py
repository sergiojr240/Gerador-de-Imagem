import cv2
import numpy as np
from .interfaces import GeradorImageStrategy

class FotogrametriaStrategy(GeradorImageStrategy):
    def processar_imagem(self, imagem):
        # Carregar a imagem
        img = cv2.imdecode(np.frombuffer(imagem.read(), np.uint8), cv2.IMREAD_COLOR)

        # Converter a imagem para escala de cinza
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Marcar pontos vermelhos na imagem
        img_with_points = self.marcar_pontos_vermelhos(img.copy())

        # Converter a imagem resultante para formato de bytes
        _, result_data = cv2.imencode('.jpg', img_with_points)
        result_bytes = result_data.tobytes()

        return result_bytes

    def marcar_pontos_vermelhos(self, img, point_size=5):
        # Gerar pontos vermelhos na imagem
        rows, cols = img.shape[:2]
        for _ in range(40):
            x, y = np.random.randint(0, rows), np.random.randint(0, cols)
            color = [0, 0, 255]  # Cor vermelha
            img = cv2.circle(img, (y, x), point_size, color, -1)  # Ajuste o tamanho dos pontos

        return img
        
class SegmentacaoStrategy(GeradorImageStrategy):
    def processar_imagem(self, imagem):
        # Carregar a imagem
        img = cv2.imdecode(np.frombuffer(imagem.read(), np.uint8), cv2.IMREAD_COLOR)

        # Converter a imagem para escala de cinza
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Marcar pontos vermelhos na imagem
        img_with_points = self.marcar_pontos_azuis(img.copy())

        # Converter a imagem resultante para formato de bytes
        _, result_data = cv2.imencode('.jpg', img_with_points)
        result_bytes = result_data.tobytes()

        return result_bytes

    def marcar_pontos_azuis(self, img, point_size=5):
        # Gerar pontos azuis na imagem
        rows, cols = img.shape[:2]
        for _ in range(40):
            x, y = np.random.randint(0, rows), np.random.randint(0, cols)
            color = [255, 0, 0]  # Cor azul
            img = cv2.circle(img, (y, x), point_size, color, -1)  # Ajuste o tamanho dos pontos

        return img

