import requests
import os
from dotenv import load_dotenv

load_dotenv()

ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")

def enviar_mensagem(telefone, nome):
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"
    payload = {
        "phone": telefone,
        "message": f"Olá {nome}, tudo bem com você?"
    }
    headers = {
        "Client-Token": ZAPI_CLIENT_TOKEN,
        
    }
    
    try:
        r = requests.post(url, json=payload, headers=headers)
        if r.status_code == 200:
            print(f"Mensagem enviada para {nome}")
        else:
            print(f"Erro ao enviar para {nome}: {r.status_code} - {r.text}")
    except Exception as e:
        print(f"Erro de conexão: {e}")