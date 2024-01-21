from django.shortcuts import render
from .forms import ImageUploadForm
from .models import ImageStrategy

import base64

def processar_imagem(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            imagem = form.cleaned_data['imagem']

            # Processar a imagem usando a estratégia escolhida
            image_strategy = ImageStrategy()
            tipo_estrategia = request.POST.get('tipo_estrategia', 'fotogrametria')
            resultado = image_strategy.processar_imagem(imagem, tipo_estrategia)

            # Converter os bytes para base64
            resultado_base64 = base64.b64encode(resultado).decode('utf-8')

            return render(request, 'resultado.html', {'resultado': resultado_base64})
    else:
        form = ImageUploadForm()

    return render(request, 'processar_imagem.html', {'form': form})


