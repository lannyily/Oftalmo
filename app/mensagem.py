import urllib.parse
from django.conf import settings
import webbrowser

def enviar_mensagem_whatsapp(consulta):
    """Envia mensagem via WhatsApp Web usando a API web diretamente"""
    try:
        # Formatação do número
        numero = ''.join(filter(str.isdigit, consulta.telefone))
        if len(numero) == 11:
            numero = f'55{numero}'  # Removemos o + para a URL
            
        # Formatação da mensagem
        mensagem = (
            f"Olá {consulta.nome}! Sua consulta com {consulta.medico.nome} "
            f"foi confirmada para {consulta.data_atribuida.strftime('%d/%m/%Y')}.\n\n"
            f"🕑 *Turno:* {consulta.turno}\n"
            f"🧑‍⚕️ *Médico:* Dr(a). {consulta.medico.nome}\n"
            f"📄 *Procedimento:* {consulta.procedimento}\n"
            "Por favor, chegue com 10 minutos de antecedência.\n"
            "Se deseja mudar a data do procedimento?\n\n"
            "Atenciosamente,\nEquipe Clínica"
        )
        
        # Codifica a mensagem para URL
        mensagem_codificada = urllib.parse.quote(mensagem)
        
        # Abre no navegador padrão
        url = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem_codificada}"
        webbrowser.open(url)
        
        return True
            
    except Exception as e:
        print(f"❌ Erro no envio: {str(e)}")
        return False