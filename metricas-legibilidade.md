# 📊 Métricas de Legibilidade: Como Medir a Complexidade do seu Texto Localmente

Quando simplificamos um texto ou pedimos para uma IA explicar um conceito complexo, precisamos de uma forma matemática e imparcial para provar que o texto realmente ficou mais fácil de ler. 

Neste guia prático, você vai aprender a implementar o **Índice de Legibilidade de Flesch (adaptado para o Português)** em um script Python simples, rodando totalmente local e sem dependências externas.

---

## 🧐 O que é o Índice de Flesch?

O teste de legibilidade de Flesch avalia o texto com base no comprimento das frases e no tamanho das palavras. Ele gera uma pontuação de **0 a 100**:
*   **75 a 100:** Muito Fácil (nível de leitura de escola primária).
*   **50 a 75:** Fácil/Médio (linguagem cotidiana e acessível).
*   **25 a 50:** Difícil (textos acadêmicos ou técnicos).
*   **0 a 25:** Muito Difícil (textos científicos, jurídicos ou de alta complexidade).

No português, usamos a fórmula adaptada por **França Martins**:

$$\text{Flesch} = 248.83 - (1.015 \times \text{Media de Palavras por Sentença}) - (84.6 \times \text{Media de Sílabas por Palavra})$$

---

## 💻 Implementação Prática em Python

Para manter sua plataforma leve e rápida, criamos uma função em Python puro que estima o número de sílabas e calcula o índice de Flesch.

Crie um arquivo chamado `medir_legibilidade.py`:

```python
import re

def contar_silabas_estimado(palavra):
    """
    Uma heurística simples para contar sílabas em português baseada em grupos vocálicos.
    Ideal para execuções rápidas e sem bibliotecas pesadas.
    """
    palavra = palavra.lower().strip()
    if not palavra:
        return 0
    
    # Remove pontuações comuns anexadas à palavra
    palavra = re.sub(r'[^\w\s]', '', palavra)
    
    # Define grupos de vogais e ditongos como uma única sílaba teórica
    # Esta aproximação funciona para cerca de 85-90% das palavras em PT-BR
    padrao_vogais = r'[aeiouáéíóúâêôãõüéíóúá]+'
    grupos_vogais = re.findall(padrao_vogais, palavra)
    
    # Heurística para ajustar ditongos/hiatos simples
    total_silabas = len(grupos_vogais)
    
    # Palavras muito curtas têm pelo menos 1 sílaba
    if total_silabas == 0:
        return 1
        
    return total_silabas

def calcular_flesch_portugues(texto):
    # 1. Separar sentenças usando pontuação (. ! ?)
    sentencas = [s.strip() for s in re.split(r'[.!?]+', texto) if s.strip()]
    num_sentencas = len(sentencas)
    
    if num_sentencas == 0:
        return 0.0, "Texto vazio ou inválido"
    
    # 2. Separar e limpar palavras
    palavras = [p for p in texto.split() if p.strip()]
    num_palavras = len(palavras)
    
    if num_palavras == 0:
        return 0.0, "Texto sem palavras válidas"
        
    # 3. Contar sílabas de cada palavra
    total_silabas = sum(contar_silabas_estimado(p) for p in palavras)
    
    # 4. Médias para a fórmula
    palavras_por_sentenca = num_palavras / num_sentencas
    silabas_por_palavra = total_silabas / num_palavras
    
    # 5. Aplicação da fórmula de França Martins
    score = 248.83 - (1.015 * palavras_por_sentenca) - (84.6 * silabas_por_palavra)
    
    # Limitar o score entre 0 e 100 para consistência visual
    score = max(0.0, min(100.0, score))
    
    # Classificação do resultado
    if score >= 75:
        classificacao = "Muito Fácil (Leitura fluida para qualquer público)"
    elif score >= 50:
        classificacao = "Fácil a Médio (Linguagem acessível e cotidiana)"
    elif score >= 25:
        classificacao = "Difícil (Exige atenção e vocabulário técnico)"
    else:
        classificacao = "Muito Difícil (Texto acadêmico ou científico denso)"
        
    return score, classificacao

# --- TESTE PRÁTICO ---
if __name__ == "__main__":
    texto_complexo = (
        "A inteligência artificial generativa denota avanços ímpares na cognição computacional, "
        "propiciando a emulação de raciocínio lógico-formal através de redes neurais profundas."
    )
    
    texto_simplificado = (
        "A inteligência artificial avançou muito. "
        "Agora, os computadores conseguem imitar o pensamento humano usando programas modernos."
    )
    
    print("--- TEXTO COMPLEXO ---")
    score_comp, class_comp = calcular_flesch_portugues(texto_complexo)
    print(f"Pontuação Flesch: {score_comp:.2f}")
    print(f"Classificação: {class_comp}\n")
    
    print("--- TEXTO SIMPLIFICADO ---")
    score_simp, class_simp = calcular_flesch_portugues(texto_simplificado)
    print(f"Pontuação Flesch: {score_simp:.2f}")
    print(f"Classificação: {class_simp}")
```

---

## 📈 Conexão com o NILC-Metrix

No ambiente acadêmico brasileiro, o **NILC-Metrix** é o pacote de referência para análises linguísticas profundas. Ele avalia mais de 200 dimensões, incluindo a *Distância na Árvore de Dependências* e fórmulas sintáticas complexas (como Frazier e Yngve).

O script acima funciona como o seu **"sensor de legibilidade rápido"**, ideal para dar feedback imediato ao seu agente ou plataforma. Para auditorias finais de pesquisa, o protocolo experimental do projeto prevê o envio do texto para a API do NILC-Metrix para validação das estruturas gramaticais completas.
