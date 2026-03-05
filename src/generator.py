from src.api_client import get_groq_client
from src.prompt_engine import PromptEngine

class ContentGenerator:
    def __init__(self, perfil_aluno):
        self.client = get_groq_client()
        self.engine = PromptEngine(perfil_aluno)
        self.model = "llama-3.3-70b-versatile" 

    def _chamar_api(self, prompt):
        """Função auxiliar para evitar repetição de código"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def gerar_explicacao(self, topico):
        prompt = self.engine.preparar_prompt_explicacao(topico)
        return self._chamar_api(prompt)

    def gerar_exemplos(self, topico):
        prompt = self.engine.prompt_exemplos(topico)
        return self._chamar_api(prompt)

    def gerar_perguntas(self, topico):
        prompt = self.engine.prompt_perguntas(topico)
        return self._chamar_api(prompt)

    def gerar_resumo(self, topico):
        prompt = self.engine.prompt_resumo_visual(topico)
        return self._chamar_api(prompt)