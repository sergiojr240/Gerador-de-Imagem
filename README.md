# ImageProcessing Framework

Este é um framework Django simples que demonstra o padrão de estratégia para processamento de imagem.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `image_processor/`: Aplicativo Django que contém as visualizações, modelos, estratégias, etc.
- `ImageProcessing/`: Projeto principal do Django.
- `migrations/`: Diretório padrão para migrações do Django.
- `manage.py`: Script de gerenciamento do Django.

## Componentes Principais

- **`image_processor.models`**: Contém modelos relacionados ao processamento de imagem.
- **`image_processor.strategies`**: Implementações de estratégias para processamento de imagem.
- **`image_processor.views`**: Visualizações para manipulação de requisições relacionadas ao processamento de imagem.

## Como Executar

Para executar o projeto localmente, siga estas etapas:

1. Clone o repositório: `git clone https://github.com/seu-usuario/ImageProcessing.git`
2. Instale as dependências: `pip install -r requirements.txt`
3. Execute as migrações: `python manage.py migrate`
4. Inicie o servidor: `python manage.py runserver`

Acesse [http://127.0.0.1:8000/processador-imagem/](http://127.0.0.1:8000/processador-imagem/) para testar o framework.


