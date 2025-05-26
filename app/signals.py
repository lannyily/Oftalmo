from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Consulta
from .mensagem import enviar_mensagem_whatsapp
import time

@receiver(post_save, sender=Consulta)
def enviar_whatsapp_apos_confirmacao(sender, instance, created, **kwargs):
    if not created and instance.confirmada:
        try:
            # Tenta enviar 3 vezes antes de desistir
            for tentativa in range(3):
                try:
                    enviar_mensagem_whatsapp(instance)
                    print(f"✅ WhatsApp enviado para {instance.nome}")
                    break
                except Exception as e:
                    print(f"❌ Tentativa {tentativa + 1} falhou: {e}")
                    time.sleep(5)  # Espera 5 segundos antes de tentar novamente
        except Exception as e:
            print(f"🚨 Falha definitiva ao enviar para {instance.nome}: {e}")