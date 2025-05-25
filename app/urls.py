from django.urls import path
from .views.home_views import home_view
from .views.formulario_views import formulario_view
from .views.medicos_views import medicos_view
from .views.perfilMedico_views import perfilMedico_views
from .views.perfilProcedimento_views import perfilProcedimento_views
from .views.procedimentos_views import procedimentos_views
from .views.formulario_views import formularioConsulta_view

urlpatterns = [
    path('', home_view, name='home'),
    path('formulario/', formulario_view, name='formulario'),
    path('formularioConsulta/', formularioConsulta_view, name='formularioConsulta'),
    path('medicos/', medicos_view, name='medicos'),
    path('medico/<str:nome>/', perfilMedico_views, name='perfilMedico'),
    path('procedimento/<str:nome>/', perfilProcedimento_views, name='perfilProcedimento'),
    path('procedimentos/', procedimentos_views, name='procedimentos'),
]