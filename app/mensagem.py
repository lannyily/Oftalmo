from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.parse
import time
import os
from pathlib import Path

# Configuração do diretório de sessão
BASE_DIR = Path(__file__).resolve().parent.parent
WHATSAPP_SESSION_DIR = os.path.join(BASE_DIR, 'whatsapp_session')
os.makedirs(WHATSAPP_SESSION_DIR, exist_ok=True)

# Variável global do driver (agora definida corretamente)
driver_global = None

def iniciar_driver():
    """Inicia o driver do Chrome com configurações personalizadas"""
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={WHATSAPP_SESSION_DIR}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")  # Reduz logs do Chrome
    
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    except Exception as e:
        print(f"Erro ao iniciar Chrome: {e}")
        raise

def verificar_conexao_whatsapp(driver):
    """Verifica se o WhatsApp Web está conectado"""
    try:
        driver.get("https://web.whatsapp.com")
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@role="textbox"]'))
        )
        return True
    except:
        return False

def enviar_mensagem_whatsapp(consulta):
    """Envia mensagem via WhatsApp Web"""
    global driver_global
    
    try:
        # Inicia ou reutiliza o driver
        if driver_global is None or not verificar_conexao_whatsapp(driver_global):
            if driver_global:
                driver_global.quit()
            driver_global = iniciar_driver()
        
        # Formatação do número
        numero = ''.join(filter(str.isdigit, consulta.telefone))
        if len(numero) == 11:
            numero = f'55{numero}'
            
        # Formatação da mensagem
        mensagem = urllib.parse.quote(
            f"Olá, {consulta.nome}! Tudo bem? 😊\n\n"
            f"Sua consulta está confirmada para {consulta.data_atribuida.strftime('%d/%m/%Y')} com Dr(a). {consulta.medico.nome} na Clínica Oftalmo+.\n\n"
            "Por favor, chegue com 10 minutos de antecedência.\n\n"
            "Se precisar reagendar, fale conosco.\n\n"
            "Atenciosamente,\nEquipe Oftalmo+"
        )
        
        # Envio da mensagem
        driver_global.get(f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}")
        
        campo_msg = WebDriverWait(driver_global, 15).until(
            EC.presence_of_element_located((By.XPATH, '//div[@role="textbox"][@data-tab="10"]'))
        )
        time.sleep(1)  # Pequena pausa para estabilização
        campo_msg.send_keys(Keys.ENTER)
        time.sleep(2)  # Garante o envio
        
        # Verifica se a mensagem foi enviada
        WebDriverWait(driver_global, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[@data-testid="msg-time"]'))
        )
        
        print(f"✅ Mensagem enviada para {consulta.nome}")
        return True
        
    except Exception as e:
        print(f"❌ Erro no envio: {str(e)}")
        if driver_global:
            driver_global.quit()
            driver_global = None
        return False