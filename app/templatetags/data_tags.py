from django import template
from ..models import ProcedimentoDestaque

register = template.Library()

@register.simple_tag
def get_procedimentos_destaque():
    return [d.procedimento for d in ProcedimentoDestaque.objects.select_related('procedimento').order_by('ordem')[:4]]