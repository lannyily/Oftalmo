from django.contrib import admin
from .models import Medico, Procedimento, ProcedimentoDestaque, MedicoDestaque, Consulta, ConsultaConfirmada
from django.contrib.admin import DateFieldListFilter

@admin.register(ConsultaConfirmada)
class ConsultaConfirmadaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'medico', 'dia', 'data_atribuida', 'criado_em']
    list_filter = [
        'dia',
        'medico',
        ('data_atribuida', DateFieldListFilter),
    ]
    search_fields = ['nome', 'email', 'cpf']

    def get_queryset(self, request):
        return super().get_queryset(request).filter(confirmada=True)

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'medico', 'dia', 'confirmada', 'data_atribuida', 'criado_em']
    list_filter = ['dia', 'medico', 'confirmada']
    search_fields = ['nome', 'email', 'cpf']

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero_cmr', 'especialidades', 'atendimento', 'diferenciais', 'formacao')
    search_fields = ('nome', 'especialidades')

@admin.register(Procedimento)
class ProcedimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'tempo_procedimento', 'descricao', 'informacao_internacao', 'informacao_recuperacao')
    list_filter = ('tipo',)
    search_fields = ('nome', 'descricao')

@admin.register(ProcedimentoDestaque)
class ProcedimentoDestaqueAdmin(admin.ModelAdmin):
    list_display = ('procedimento', 'ordem', 'data_criacao')
    list_editable = ('ordem',)
    ordering = ('ordem',)
    
    def has_add_permission(self, request):
        return self.model.objects.count() < 4

@admin.register(MedicoDestaque)
class MedicoDestaqueAdmin(admin.ModelAdmin):
    list_display = ('medico', 'ordem', 'data_criacao')
    list_editable = ('ordem',)
    
    def has_add_permission(self, request):
        return self.model.objects.count() < 3