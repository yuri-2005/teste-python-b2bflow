from src.supabase_client import buscar_contatos

if __name__ == "__main__":
    contatos = buscar_contatos()

    if contatos:
        print("Contatos encontrados:")
        for contato in contatos:
            print(contato)
    else:
        print("Não foi possível carregar os contatos ou a tabela está vazia.")