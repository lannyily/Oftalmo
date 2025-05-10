from django.urls import path
from .views.home_views import home_view
from .views.formulario_views import formulario_view
from .views.medicos_views import medicos_view
from .views.perfilMedico_views import perfilMedico_views
from .views.perfilProcedimento_views import perfilProcedimento_views
from .views.procedimentos_views import procedimentos_views

urlpatterns = [
    path('', home_view, name='home'),
    path('formulario/', formulario_view, name='formulario'),
    path('medicos/', medicos_view, name='medicos'),
    path('perfil-medico/', perfilMedico_views, name='perfil-medico'),
    path('perfil-procedimento/', perfilProcedimento_views, name='perfil-procedimento'),
    path('procedimentos/', procedimentos_views, name='procedimentos'),
]