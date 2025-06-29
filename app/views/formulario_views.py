from django.shortcuts import render, redirect, get_object_or_404
from ..models import Medico
from ..models import Consulta, Procedimento, HorarioProcedimento
from django.http import JsonResponse

def procedimentos_por_tipo(request):
    tipo = request.GET.get('tipo')
    procedimentos = Procedimento.objects.filter(tipo=tipo).values('id', 'nome')
    return JsonResponse(list(procedimentos), safe=False)

def dias_por_procedimento(request):
    procedimento_id = request.GET.get('procedimento_id')
    dias = HorarioProcedimento.objects.filter(procedimento_id=procedimento_id).values_list('dia', flat=True).distinct()
    return JsonResponse(list(dias), safe=False)

def turnos_por_procedimento_dia(request):
    procedimento_id = request.GET.get('procedimento_id')
    dia = request.GET.get('dia')
    turnos = HorarioProcedimento.objects.filter(procedimento_id=procedimento_id, dia=dia).values_list('turno', flat=True).distinct()
    return JsonResponse(list(turnos), safe=False)

def medicos_por_procedimento(request):
    procedimento_id = request.GET.get('procedimento_id')
    medicos = Medico.objects.filter(procedimentos__id=procedimento_id).values('id', 'nome')
    return JsonResponse(list(medicos), safe=False)

def formulario_view(request):
    return render(request, 'formulario.html')

def formularioConsulta_view(request):
    medicos = Medico.objects.all()

    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        dia = request.POST.get('dia')
        mensagem = request.POST.get('mensagem')

        medico_id = request.POST.get('medico')
        medico = get_object_or_404(Medico, id=medico_id)


        Consulta.objects.create(
            nome=nome,
            telefone=telefone,
            email=email,
            cpf=cpf,
            dia=dia,
            medico=medico,
            mensagem=mensagem
        )

        return render(request, 'formularioConsulta.html', {
            'medicos': medicos,
            'mensagem_sucesso': 'Solicitação enviada com sucesso!'
        })

    return render(request, 'formularioConsulta.html', {'medicos': medicos})