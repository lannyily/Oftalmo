from django.shortcuts import render
from ..models import MedicoDestaque, ProcedimentoDestaque


def home_view(request):
    # Médicos em destaque (máximo 3)
    medicos_destaque = [
        md.medico for md in 
        MedicoDestaque.objects.select_related('medico').order_by('ordem')[:3]
        if hasattr(md, 'medico')
    ]
    
    # Procedimentos em destaque (máximo 4)
    procedimentos_destaque = [
        pd.procedimento for pd in 
        ProcedimentoDestaque.objects.select_related('procedimento').order_by('ordem')[:4]
        if hasattr(pd, 'procedimento')
    ]
    
    return render(request, 'home.html', {
        'medicos_destaque': medicos_destaque,
        'procedimentos_destaque': procedimentos_destaque
    })