from django.shortcuts import render
from django.db.models import Q
from ..models import Procedimento, Medico

def procedimentos_views(request):
    query = request.GET.get('q', '')
    tipos_selecionados = request.GET.getlist('tipo')
    medico_id = request.GET.get('medico')

    procedimentos = Procedimento.objects.all()
    medicos = Medico.objects.all()

    if query:
        procedimentos = procedimentos.filter(
            Q(nome__icontains=query) | Q(descricao__icontains=query)
        )

    if tipos_selecionados:
        procedimentos = procedimentos.filter(tipo__in=tipos_selecionados)

    if medico_id:
        procedimentos = procedimentos.filter(medicos__id=medico_id)

    return render(request, 'procedimentos.html', {
        'procedimentos': procedimentos,
        'medicos': medicos,
        'tipos_selecionados': tipos_selecionados,
        'medico_selecionado': medico_id,
        'total_resultados': procedimentos.count(),
    })