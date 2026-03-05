import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_groq_client():
    """
    Inicializa e retorna o cliente Groq configurado.
    """
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        raise ValueError("ERRO: A variável GROQ_API_KEY não foi encontrada no arquivo .env")
        
    return OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=api_key
    )