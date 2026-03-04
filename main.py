from google import genai

# Substitua pelasua chave entre as aspas
CHAVE_API = "AIzaSyCGZsob72pEvvWnx8HbNCXQjTB58-6oEU4"

client = genai.Client(api_key=CHAVE_API)

try:
    print("Conectando ao Gemini...")
    
    # Vamos usar o modelo 2.0 Flash que é o mais rápido e estável para o plano grátis
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents="O que é um átomo? Responda em uma frase curta para teste."
    )

    print("\nSucesso! Resposta do Gemini:")
    print(response.text)

except Exception as e:
    print(f"\nErro ao testar a API do Gemini: {e}")
    print("Verifique se a chave está correta ou se há restrições na sua rede.")