from django.shortcuts import render, redirect, get_object_or_404
from ..models import Procedimento

def perfilProcedimento_views(request, nome):
    procedimento = get_object_or_404(Procedimento, nome=nome)
    return render(request, 'perfilProcedimento.html', {
        'procedimento': procedimento
    })