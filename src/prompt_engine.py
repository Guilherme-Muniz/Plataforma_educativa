class PromptEngine:
    def __init__(self,perfil_aluno):
        """
        Recebe um dicionário com os dados do aluno vindos do JSON.
        """
        self.aluno = perfil_aluno

    def _gerar_base_prompt(self):
        """
        Gera uma base geral para o prompt, para depoi anexar o tópico em outra função
        """
        return (
            f"Você é um professor experiente em Pedagogia adaptando conteúdo para um aluno específico. "
            f"Dados do Aluno: Nome: {self.aluno['nome']}, Idade: {self.aluno['idade']} anos, "
            f"Nível: {self.aluno['nivel']}, Estilo de Aprendizado: {self.aluno['estilo_aprendizado']}."
        )
    
    def preparar_prompt_explicacao(self, topico):
        """
        Junção da base com o tópico específico para gerar a explicação principal
        """
        base = self._gerar_base_prompt()
        instrucao = (
            f"\nExplique o tópico '{topico}' de forma didática. "
            "Pense passo a passo para garantir que a lógica seja clara para a idade do aluno, seu nível e ao estilo ao qual ele prefere aprender. "
            "Não pule etapas na explicação.")
        return base + instrucao
    
    def prompt_exemplos(self, topico):
        """
        Junção da base com o tópico específico para a criação de 3 exemplos personalizados
        """
        base = self._gerar_base_prompt()
        instrucao = (
            f"\nCrie 3 exemplos práticos de '{topico}'. "
            f"Os exemplos devem ser do cotidiano de uma pessoa de {self.aluno['idade']} anos"
        )
        return base + instrucao
    
    def prompt_perguntas(self, topico):
        """
        Junção da base com o tópico específico para a criação de perguntas retóricas
        """
        base = self._gerar_base_prompt()
        instrucao = (
            f"\nCrie 3 perguntas de reflexão sobre '{topico}' que estimulem o pensamento crítico de um aluno de nível {self.aluno['nivel']} e idade {self.aluno['idade']}."
        )
        return base + instrucao
    
    def prompt_resumo_visual(self, topico):
        """
        Junção da base com o tópico específico para a criação de  um resumo visual usando caracteres ASCII
        """
        base = self._gerar_base_prompt()
        instrucao = (
            f"\nCrie um resumo visual de '{topico}' no formato de mapa mental usando apenas caracteres ASCII."
            "A estrutura deve ser clara e organizada"
        )
        return base + instrucao