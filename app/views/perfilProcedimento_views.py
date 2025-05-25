from django.shortcuts import render, redirect, get_object_or_404
from ..models import Procedimento
from ..models import Medico

def perfilProcedimento_views(request, nome):
    procedimento = get_object_or_404(Procedimento, nome=nome)
    medicos = procedimento.medicos.all()
    return render(request, 'perfilProcedimento.html', {
        'procedimento': procedimento,
        'medicos': medicos,
    })