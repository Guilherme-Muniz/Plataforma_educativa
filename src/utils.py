import json
import os
from datetime import datetime

def salvar_resultado_json(aluno, topico, conteudos):
    """
    Salva o conteúdo gerado em um arquivo JSON estruturado.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"samples/resultado_{aluno['nome']}_{timestamp}.json"
    
    # Garante que a pasta samples existe
    os.makedirs('samples', exist_ok=True)
    
    dados_para_salvar = {
        "metadata": {
            "aluno": aluno["nome"],
            "idade": aluno["idade"],
            "topico": topico,
            "data_geracao": timestamp
        },
        "conteudo": conteudos
    }
    
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados_para_salvar, f, indent=2, ensure_ascii=False)
    
    return nome_arquivo

def carregar_perfis():
    """Carrega os perfis de alunos do arquivo JSON"""
    with open('data/perfis_alunos.json', 'r', encoding='utf-8') as f:
        return json.load(f)