from django.urls import path
from .views.home_views import home_view
from .views.formulario_views import formulario_view
from .views.medicos_views import medicos_view
from .views.perfilMedico_views import perfilMedico_views
from .views.perfilProcedimento_views import perfilProcedimento_views
from .views.procedimentos_views import procedimentos_views
from .views.formulario_views import formularioConsulta_view, procedimentos_por_tipo, dias_por_procedimento, turnos_por_procedimento_dia, medicos_por_procedimento

urlpatterns = [
    path('', home_view, name='home'),
    path('formulario/', formulario_view, name='formulario'),
    path('ajax/procedimentos/', procedimentos_por_tipo, name='ajax_procedimentos'),
    path('ajax/dias/', dias_por_procedimento, name='ajax_dias'),
    path('ajax/turnos/', turnos_por_procedimento_dia, name='ajax_turnos'),
    path('ajax/medicos/', medicos_por_procedimento, name='ajax_medicos'),
    path('formularioConsulta/', formularioConsulta_view, name='formularioConsulta'),
    path('medicos/', medicos_view, name='medicos'),
    path('medico/<str:nome>/', perfilMedico_views, name='perfilMedico'),
    path('procedimento/<str:nome>/', perfilProcedimento_views, name='perfilProcedimento'),
    path('procedimentos/', procedimentos_views, name='procedimentos'),
]