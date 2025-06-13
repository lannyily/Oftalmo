from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Consulta
import time
from django.conf import settings

@receiver(post_save, sender=Consulta)
def enviar_whatsapp_apos_confirmacao(sender, instance, created, **kwargs):
    if not created and instance.confirmada:
        if not getattr(settings, 'WHATSAPP_ENABLED', False):
            return
            
        # Usando a abordagem 1 (recomendada)
        from .mensagem import enviar_mensagem_whatsapp
        
        max_tentativas = 3
        for tentativa in range(max_tentativas):
            try:
                if enviar_mensagem_whatsapp(instance):
                    print(f"✅ Mensagem preparada para {instance.nome}")
                    break
                print(f"⚠️ Falha no envio para {instance.nome} (tentativa {tentativa + 1})")
            except Exception as e:
                print(f"❌ Erro na tentativa {tentativa + 1}: {str(e)}")
            
            if tentativa < max_tentativas - 1:
                time.sleep(2)
        else:
            print(f"🚨 Falha ao preparar mensagem para {instance.nome}")