from django.shortcuts import render, redirect, get_object_or_404
from ..models import Medico
from ..models import Consulta

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