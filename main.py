from src.supabase_client import buscar_contatos
from src.zapi_client import enviar_mensagem

contatos = buscar_contatos()

for contato in contatos:
    enviar_mensagem(contato["telefone"], contato["nome"])
