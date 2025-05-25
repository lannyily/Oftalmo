from django.shortcuts import render, redirect, get_object_or_404

def formulario_view(request):
    return render(request, 'formulario.html')