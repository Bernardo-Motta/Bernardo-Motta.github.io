"""
Teste local — Tucano-1b1-Instruct (modelo nativo em português)
====================================================
Projeto: Metodologia de Sistematização e Avaliação de GenAI em Português (UFSJ)

Família Tucano (TucanoBR, Univ. Bonn): decoders treinados do zero em português
brasileiro (corpus GigaVerbo). A versão 1.1B Instruct roda em CPU, mas é mais lenta que
o TeenyTinyLlama. Para algo mais leve, troque MODELO por "TucanoBR/Tucano-630m" (base).
Fonte: https://huggingface.co/TucanoBR/Tucano-1b1-Instruct

Pré-requisitos:
  pip install transformers torch

Uso:
  python run_tucano_local.py
  python run_tucano_local.py simplificacao
"""

import sys
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODELO = "TucanoBR/Tucano-1b1-Instruct"

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


def carregar_modelo():
    tokenizer = AutoTokenizer.from_pretrained(MODELO)
    modelo = AutoModelForCausalLM.from_pretrained(MODELO)
    dispositivo = "cuda" if torch.cuda.is_available() else "cpu"
    modelo.to(dispositivo)
    return tokenizer, modelo, dispositivo


def rodar(tarefa: str, prompt: str, tokenizer, modelo, dispositivo) -> None:
    print(f"\n{'=' * 60}\nTAREFA: {tarefa}\n{'=' * 60}")
    entrada = tokenizer(prompt, return_tensors="pt").to(dispositivo)
    saida = modelo.generate(**entrada, max_new_tokens=200, do_sample=True, temperature=0.7)
    print(tokenizer.decode(saida[0], skip_special_tokens=True))


if __name__ == "__main__":
    tokenizer, modelo, dispositivo = carregar_modelo()
    alvo = sys.argv[1] if len(sys.argv) > 1 else None
    if alvo:
        if alvo not in PROMPTS:
            print(f"Tarefa desconhecida. Opções: {list(PROMPTS.keys())}")
            sys.exit(1)
        rodar(alvo, PROMPTS[alvo], tokenizer, modelo, dispositivo)
    else:
        for tarefa, prompt in PROMPTS.items():
            rodar(tarefa, prompt, tokenizer, modelo, dispositivo)
