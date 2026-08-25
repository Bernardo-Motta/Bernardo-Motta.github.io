# 💻 Códigos e Scripts de Teste

Aqui você encontra os scripts de código prontos para rodar no seu computador. Eles servem para testar modelos locais e avaliar automaticamente a qualidade e a legibilidade dos textos gerados.

---

## 🐍 1. Teste de Modelo Local (Ollama + Qwen)

Este script em Python faz uma chamada local para o modelo **Qwen 2.5 (7B)** rodando no seu computador através do Ollama [1, 2]. Ele envia um texto complexo e solicita uma simplificação direta ao modelo.

### Código-Fonte (`teste_ollama.py`):

```python
import requests

def testar_modelo_local(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "qwen2.5:7b",
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        print("Resposta do Modelo:")
        print(response.json().get("response"))
    except Exception as e:
        print(f"Erro ao conectar ao Ollama: {e}")

if __name__ == "__main__":
    testar_modelo_local("Simplifique: 'A inteligência artificial generativa denota avanços ímpares.'")
```

### Como Executar:
1. Certifique-se de ter o [Ollama](https://ollama.com) instalado e rodando no seu computador.
2. Baixe o modelo executando no seu terminal: `ollama run qwen2.5:7b`.
3. Instale a biblioteca de requisições: `pip install requests`.
4. Salve o código acima em um arquivo chamado `teste_ollama.py`.
5. Execute com o comando: `python teste_ollama.py`.

---

## 📊 2. Cálculo do Índice de Legibilidade de Flesch (PT-BR)

Este segundo script mede a complexidade de qualquer texto em português. Ele analisa a quantidade de palavras por sentença e estima as sílabas das palavras para calcular o **Score de Flesch**, classificando o texto de "Muito Fácil" a "Muito Difícil".

### Código-Fonte (`calculo_legibilidade.py`):

```python
import re

def contar_silabas_palavra(palavra):
    # Uma heurística para contagem de sílabas em português baseada em grupos vocálicos
    palavra = palavra.lower().strip()
    if not palavra:
        return 0
    # Remove caracteres que não são letras
    palavra = re.sub(r'[^a-záéíóúâêôãõüçíý]', '', palavra)
    # Encontra os agrupamentos de vogais
    vogais = re.findall(r'[aeiouáéíóúâêôãõüíý]+', palavra)
    count = len(vogais)
    return max(1, count)

def calcular_flesch_pt(texto):
    texto = texto.strip()
    if not texto:
        return 0.0, "Texto vazio"

    # 1. Conta sentenças buscando pontos finais, exclamações e interrogações
    sentencas = [s for s in re.split(r'[.!?]+', texto) if s.strip()]
    num_sentencas = max(1, len(sentencas))

    # 2. Divide em palavras limpas
    palavras_limpas = [re.sub(r'[^\w]', '', p) for p in texto.split()]
    palavras = [p for p in palavras_limpas if p]
    num_palavras = max(1, len(palavras))

    # 3. Soma as sílabas de cada palavra
    total_silabas = sum(contar_silabas_palavra(p) for p in palavras)

    # Cálculo das médias (ASL = Palavras/Frase | ASW = Sílabas/Palavra)
    asl = num_palavras / num_sentencas
    asw = total_silabas / num_palavras

    # Fórmula clássica adaptada para o Português Brasileiro
    score = 248.83 - (1.015 * asl) - (84.6 * asw)

    # Classificação por facilidade de leitura
    if score >= 75:
        nivel = "Muito Fácil (Adequado para Ensino Fundamental I - até 5º ano)"
    elif score >= 50:
        nivel = "Fácil a Médio (Adequado para Ensino Fundamental II - 6º ao 9º ano)"
    elif score >= 30:
        nivel = "Difícil (Adequado para Ensino Médio/Universitário)"
    else:
        nivel = "Muito Difícil (Adequado para Pós-Graduação/Acadêmico)"

    return score, nivel, num_sentencas, num_palavras, total_silabas

if __name__ == "__main__":
    # Exemplo de teste prático
    texto_teste = (
        "A inteligência artificial generativa denota avanços ímpares. "
        "Sistemas multiagentes coordenam tarefas complexas sem esforço humano. "
        "Isso torna o aprendizado mais acessível e prático para todos."
    )
    
    score, nivel, s_count, w_count, syl_count = calcular_flesch_pt(texto_teste)
    
    print("--- RESULTADO DA AVALIAÇÃO DE LEGIBILIDADE ---")
    print(f"Sentenças: {s_count} | Palavras: {w_count} | Sílabas estimadas: {syl_count}")
    print(f"Score Flesch-Sabor (PT-BR): {score:.2f}")
    print(f"Classificação: {nivel}")
```

### Como Executar:
1. Você não precisa instalar nenhuma biblioteca externa, pois este script usa apenas recursos nativos do Python!
2. Salve o código acima em um arquivo chamado `calculo_legibilidade.py`.
3. Abra o terminal na pasta do arquivo e digite: `python calculo_legibilidade.py`.
4. Para testar outros textos, basta editar a variável `texto_teste` diretamente no arquivo.
