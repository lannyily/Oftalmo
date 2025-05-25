from django.shortcuts import render, redirect, get_object_or_404
from ..models import Medico


def medicos_view(request):
    medicos = Medico.objects.all()
    return render(request, 'medicos.html', {'medicos': medicos})