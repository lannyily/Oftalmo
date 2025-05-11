from django import forms
from django.core.exceptions import ValidationError
from .models import Procedimento

class DestaqueForm(forms.ModelForm):
    class Meta:
        model = Procedimento
        fields = ['em_destaque']
    
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('em_destaque'):
            count = Procedimento.objects.filter(em_destaque=True).count()
            if count >= 4 and not self.instance.em_destaque:
                raise ValidationError("Já existem 4 procedimentos em destaque. Remova um antes de adicionar outro.")
        return cleaned_data