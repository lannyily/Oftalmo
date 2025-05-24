from django.shortcuts import render
from django.db.models import Q
from ..models import Procedimento

def procedimentos_views(request):
    query = request.GET.get('q', '')
    tipos_selecionados = request.GET.getlist('tipo')

    procedimentos = Procedimento.objects.all()

    if query:
        procedimentos = procedimentos.filter(
            Q(nome__icontains=query) | Q(descricao__icontains=query)
        )

    if tipos_selecionados:
        procedimentos = procedimentos.filter(tipo__in=tipos_selecionados)

    return render(request, 'procedimentos.html', {
        'procedimentos': procedimentos,
        'tipos_selecionados': tipos_selecionados,
        'total_resultados': procedimentos.count(),  # <-- AQUI
    })