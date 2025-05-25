from django.shortcuts import render, redirect, get_object_or_404
from ..models import Medico

def perfilMedico_views(request, nome):
    medico = Medico.objects.filter(nome=nome).first()
    if not medico:
        raise Http404("Médico não encontrado")
    return render(request, 'perfilMedico.html', {
        'medico': medico,
    })
