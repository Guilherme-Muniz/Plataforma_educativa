import sys
from src.utils import carregar_perfis, salvar_resultado_json
from src.generator import ContentGenerator

print("\n" + "="*30)
print("  PLATAFORMA EDUCATIVA IA")
print("="*30)

# Carregamento inicial dos perfis 
perfis = carregar_perfis()


# Loop principal de interação 
while True:
    print("\n1. Selecionar Aluno e Gerar Conteúdo")
    print("2. Sair")
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        # Menu de seleção de aluno 
        print("\n--- Alunos Disponíveis ---")
        for i, aluno in enumerate(perfis):
            print(f"{i + 1}. {aluno['nome']} ({aluno['idade']} anos - {aluno['nivel']})")
        
        try:
            indice = int(input("\nSelecione o número do aluno: ")) - 1
            if 0 <= indice < len(perfis):
                aluno_selecionado = perfis[indice]
            else:
                print("Número fora da lista!")
                continue
        except ValueError: #tratamento de erro caso não seja escolhido um numero
            print("Entrada inválida! Digite um número.")
            continue

        # Entrada do tópico 
        topico = input(f"\nDigite o tópico para {aluno_selecionado['nome']}: ")
        
        print(f"\n--- Gerando conteúdo para {aluno_selecionado['nome']}... ---")
        
        # Instância o gerador com o perfil escolhido
        generator = ContentGenerator(aluno_selecionado)

        try:
            # Gera os 4 tipos de conteúdo exigidos 
            resultados = {
                "explicacao_conceitual": generator.gerar_explicacao(topico),
                "exemplos_praticos": generator.gerar_exemplos(topico),
                "perguntas_reflexao": generator.gerar_perguntas(topico),
                "resumo_visual": generator.gerar_resumo(topico)
            }

            # Salva o resultado em JSON 
            caminho = salvar_resultado_json(aluno_selecionado, topico, resultados)
            
            print("\n[SUCESSO] Conteúdo gerado e salvo!")
            print(f"Arquivo: {caminho}")
            
            # Exibe apenas um trecho da explicação no terminal
            print("\n--- PRÉVIA DA EXPLICAÇÃO ---")
            print(resultados["explicacao_conceitual"][:200] + "...")

        except Exception as e:
            print(f"\n[ERRO] Falha na comunicação com a API: {e}") #creio que não seja necessario, mas caso a API falhe preciso de um tratamento de erro

    elif opcao == "2":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida!")