from django.contrib import admin
from .models import Medico, Procedimento
from .models import ProcedimentoDestaque
from .models import MedicoDestaque
from .models import Consulta
from .models import ConsultaConfirmada
from django.contrib.admin import DateFieldListFilter

@admin.register(ConsultaConfirmada)
class ConsultaConfirmadaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'medico', 'dia', 'data_atribuida', 'criado_em']
    list_filter = [
        'dia',
        'medico',
        ('data_atribuida', DateFieldListFilter),  # filtro de data exata
    ]
    search_fields = ['nome', 'email', 'cpf']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(confirmada=True)

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'medico', 'dia', 'confirmada', 'data_atribuida', 'criado_em']
    list_filter = ['dia', 'medico', 'confirmada']
    search_fields = ['nome', 'email', 'cpf']
    actions = ['confirmar_consultas']

    @admin.action(description='Confirmar consultas selecionadas')
    def confirmar_consultas(self, request, queryset):
        queryset.update(confirmada=True)


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero_cmr', 'especialidades', 'atendimento', 'diferenciais', 'formacao')
    search_fields = ('nome', 'especialidades')
    

@admin.register(Procedimento)
class ProcedimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'tempo_procedimento', 'descricao', 'tempo_procedimento', 'informacao_internacao', 'informacao_recuperacao')
    list_filter = ('tipo',)
    search_fields = ('nome', 'descricao')
    
@admin.register(ProcedimentoDestaque)
class ProcedimentoDestaqueAdmin(admin.ModelAdmin):
    list_display = ('procedimento', 'ordem', 'data_criacao')
    list_editable = ('ordem',)
    ordering = ('ordem',)
    fieldsets = (
        (None, {
            'fields': ('procedimento', 'ordem')
        }),
    )
    
    def has_add_permission(self, request):
        try:
            count = ProcedimentoDestaque.objects.count()
            return count < 4
        except:
            return True
        
@admin.register(MedicoDestaque)
class MedicoDestaqueAdmin(admin.ModelAdmin):
    list_display = ('medico', 'ordem', 'data_criacao')
    list_editable = ('ordem',)
    
    def has_add_permission(self, request):
        count = MedicoDestaque.objects.count()
        return count < 3  # Limita a 3 médicos em destaque

admin.register(Medico)
admin.register(Procedimento)