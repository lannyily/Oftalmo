from django.shortcuts import render, redirect, get_object_or_404
from ..models import Medico
from ..models import Agenda, Procedimento, HorarioProcedimento
from django.http import JsonResponse


def medicos_por_procedimento(request):
    procedimento_id = request.GET.get('procedimento_id')

    if procedimento_id == 'consulta':
        # Consulta é fixa, retorna todos os médicos
        medicos = Medico.objects.all()
    else:
        try:
            procedimento = Procedimento.objects.get(id=int(procedimento_id))
            medicos = procedimento.medicos.all()
        except (Procedimento.DoesNotExist, ValueError):
            return JsonResponse([], safe=False)

    data = [{'id': m.id, 'nome': m.nome} for m in medicos]
    return JsonResponse(data, safe=False)

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




def formulario_view(request):
    return render(request, 'formulario.html')

def formularioConsulta_view(request):
    medicos = Medico.objects.all()

    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        tipo = request.POST.get('tipo')
        procedimento_input = request.POST.get('procedimento')  # pode ser 'consulta' ou um ID numérico
        dia = request.POST.get('dia')
        turno = request.POST.get('turno')
        medico_id = request.POST.get('medico')
        mensagem = request.POST.get('mensagem')

        # 🧠 Verifica se o procedimento é 'consulta' ou um ID
        if procedimento_input == 'consulta':
            procedimento_nome = 'Consulta'
        else:
            try:
                procedimento_id = int(procedimento_input)
                procedimento_obj = Procedimento.objects.get(id=procedimento_id)
                procedimento_nome = procedimento_obj.nome
            except (ValueError, Procedimento.DoesNotExist):
                procedimento_nome = 'Desconhecido'

        # 📝 Criação da Agenda
        Agenda.objects.create(
            nome=nome,
            telefone=telefone,
            email=email,
            cpf=cpf,
            tipo=tipo,
            procedimento=procedimento_nome,
            dia=dia,
            turno=turno,
            medico_id=medico_id,
            mensagem=mensagem
        )

        return render(request, 'formularioConsulta.html', {
            'medicos': medicos,
            'mensagem_sucesso': 'Solicitação enviada com sucesso!'
        })

    return render(request, 'formularioConsulta.html', {'medicos': medicos})
