from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from functools import wraps

def perfilMedico_views(request):
    return render(request, 'perfilMedico.html')