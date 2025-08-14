# Desafio Estágio Python – B2BFlow


## Setup

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/yuri-2005/teste-python-b2bflow.git
    cd teste-python-b2bflow
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Crie o arquivo `.env`** na raiz do projeto com as seguintes variáveis:
    ```ini
    SUPABASE_URL=SEU_URL_DO_SUPABASE
    SUPABASE_KEY=SUA_CHAVE_DO_SUPABASE
    ZAPI_INSTANCE_ID=SUA_INSTANCIA_ZAPI
    ZAPI_TOKEN=SEU_TOKEN_ZAPI
    ZAPI_CLIENT_TOKEN=SEU_CLIENT_TOKEN
    ```

4.  **Configure a tabela `contatos` no Supabase:**
    * **Nome da tabela:** `contatos`
    * **Campos:**
        * `id` → `int8`, primary key, auto increment
        * `nome` → `varchar`, 
        * `telefone` → `int8`
   

---

## Como Rodar

Para executar o script, use o comando:

```bash
python main.py
```

O script buscará os contatos no Supabase e enviará a mensagem via Z-API:

```Olá {{nome_contato}}, tudo bem com você?```
