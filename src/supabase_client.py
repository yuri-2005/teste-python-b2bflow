from supabase import create_client
import os 
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def buscar_contatos():
    data = supabase.table("contatos").select("*").execute()
    return data.data

# Código para testar a função
