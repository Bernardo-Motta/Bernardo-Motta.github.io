"""
Teste local — Qwen 2.5 (7B), quantizado, via Ollama
====================================================
Projeto: Metodologia de Sistematização e Avaliação de GenAI em Português (UFSJ)

Pré-requisitos:
  1. Instalar o Ollama:        https://ollama.com/download
  2. Baixar o modelo:          ollama pull qwen2.5:7b
  3. Instalar a biblioteca:    pip install ollama

Uso:
  python run_qwen2_local.py            # roda todas as tarefas de exemplo
  python run_qwen2_local.py simplificacao   # roda só uma tarefa
"""

import sys
import ollama

MODELO = "qwen2.5:7b"

# Prompts padronizados — estrutura de 3 blocos (instrução+restrições / entrada / saída esperada)
# definida no protocolo experimental do projeto (Meses 3-4).
PROMPTS = {
    "simplificacao": """Reescreva o texto abaixo em português simples e claro, mantendo todas as
informações essenciais. Use frases curtas e vocabulário comum. Não adicione
opiniões ou informações que não estejam no texto original.

Texto original:
"O processo de fotossíntese consiste na conversão de energia luminosa em energia química, \
armazenada na forma de compostos orgânicos, mediante a atuação de organismos clorofilados."

Texto simplificado:""",

    "sumarizacao": """Resuma o texto abaixo em no máximo 3 frases, mantendo apenas as
informações mais importantes. Não adicione opiniões.

Texto original:
"O Comitê Gestor da Internet no Brasil (CGI.br) divulgou nesta semana um relatório sobre o uso \
de inteligência artificial generativa no país. O levantamento mostra crescimento expressivo no \
uso de assistentes de IA por estudantes e profissionais, mas também aponta desigualdades \
regionais no acesso a essas tecnologias, especialmente fora dos grandes centros urbanos."

Resumo:""",

    "classificacao": """Classifique o texto abaixo em uma das categorias: [Educação, Saúde, \
Tecnologia, Economia, Esporte]. Responda apenas com o nome da categoria.

Texto:
"A nova plataforma de ensino a distância usa algoritmos de recomendação para sugerir \
conteúdos personalizados a cada aluno, de acordo com seu ritmo de aprendizagem."

Categoria:""",

    "explicacao": """Explique o conceito abaixo para uma pessoa sem conhecimento técnico,
em até 4 frases, usando uma analogia simples.

Conceito:
"Modelo de linguagem quantizado"

Explicação:""",
}


def rodar(tarefa: str, prompt: str) -> None:
    print(f"\n{'=' * 60}\nTAREFA: {tarefa}\n{'=' * 60}")
    resposta = ollama.chat(
        model=MODELO,
        messages=[{"role": "user", "content": prompt}],
    )
    print(resposta["message"]["content"])


if __name__ == "__main__":
    alvo = sys.argv[1] if len(sys.argv) > 1 else None
    if alvo:
        if alvo not in PROMPTS:
            print(f"Tarefa desconhecida. Opções: {list(PROMPTS.keys())}")
            sys.exit(1)
        rodar(alvo, PROMPTS[alvo])
    else:
        for tarefa, prompt in PROMPTS.items():
            rodar(tarefa, prompt)
