"""
Teste via API — Sabiá-3 (Maritaca AI)
====================================================
Projeto: Metodologia de Sistematização e Avaliação de GenAI em Português (UFSJ)

Pré-requisitos:
  1. Criar uma chave de API em: https://plataforma.maritaca.ai
  2. Instalar a biblioteca:      pip install openai
  3. Definir a variável de ambiente com sua chave:
       export MARITACA_API_KEY="sua_chave_aqui"     (Linux/Mac)
       set MARITACA_API_KEY=sua_chave_aqui          (Windows)

A API da Maritaca é compatível com a biblioteca da OpenAI — basta apontar
o endpoint (base_url) para o servidor da Maritaca.

Uso:
  python run_sabia3_api.py                    # roda todas as tarefas de exemplo
  python run_sabia3_api.py simplificacao       # roda só uma tarefa
"""

import os
import sys
import openai

MODELO = "sabia-3"

client = openai.OpenAI(
    api_key=os.environ.get("MARITACA_API_KEY", "insira_sua_chave_aqui"),
    base_url="https://chat.maritaca.ai/api",
)

# Mesmos prompts padronizados usados nos scripts locais (Llama 3 / Qwen 2.5),
# para permitir comparação direta entre modelos sob o mesmo protocolo.
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
    resposta = client.chat.completions.create(
        model=MODELO,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=512,
    )
    print(resposta.choices[0].message.content)


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
