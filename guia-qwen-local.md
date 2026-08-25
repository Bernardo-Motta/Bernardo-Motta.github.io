# 🚀 Guia Prático: Executando o Qwen 2.5 Localmente para Avaliação de Texto

O **Qwen 2.5** é uma das famílias de modelos de linguagem pequenos (SLMs) mais eficientes do mercado atual. Ele se destaca pelo excelente equilíbrio entre custo computacional e inteligência, sendo ideal para execução em computadores locais de configuração média, sem a necessidade de gastar com APIs de nuvem.

Este guia prático mostra o passo a passo para colocar o **Qwen 2.5 (7B)** para rodar na sua máquina e utilizá-lo para testes de processamento de texto e simplificação linguística.

---

## 🛠️ Requisitos Iniciais

Para rodar o modelo de 7B (7 bilhões de parâmetros) com bom desempenho, você precisará de:
*   **Processador (CPU):** Com pelo menos 4 núcleos modernos.
*   **Memória RAM:** Mínimo de 16 GB (ou uma placa de vídeo com pelo menos 8 GB de VRAM).
*   **Espaço em disco:** Cerca de 5 GB livres para o modelo quantizado.

---

## 🏎️ Passo 1: Instalando o Ollama

O **Ollama** é uma ferramenta de código aberto que simplifica a execução de modelos de linguagem locais, gerenciando o carregamento na memória e oferecendo uma API local pronta para uso.

1.  Acesse o site oficial [ollama.com](https://ollama.com) e faça o download para o seu sistema operacional (Windows, macOS ou Linux).
2.  Instale e abra o aplicativo.
3.  No seu terminal, digite o seguinte comando para baixar e rodar o modelo automaticamente:

```bash
ollama run qwen2.5:7b
```

*Pronto! Você já pode interagir com o modelo diretamente pelo terminal.*

---

## 🐍 Passo 2: Integração com Python

Agora que o motor do modelo está rodando em segundo plano no seu computador, podemos usar um script em Python para enviar textos difíceis e pedir que a IA realize transformações linguísticas.

Primeiro, instale a biblioteca oficial do Ollama:

```bash
pip install ollama
```

### Script de Teste: `simplificador_local.py`

Crie um arquivo chamado `simplificador_local.py` e adicione o seguinte código:

```python
import ollama

def simplificar_texto(texto_complexo):
    # Prompt estruturado para guiar a IA na simplificação linguística
    prompt_sistema = (
        "Você é um assistente especialista em acessibilidade e simplificação textual em português do Brasil. "
        "Sua tarefa é ler um texto técnico ou complexo e reescrevê-lo de forma que pessoas com nível básico "
        "de alfabetismo consigam compreender perfeitamente. "
        "Siga estritamente: divida frases longas, remova jargões excessivos e prefira palavras de fácil visualização."
    )
    
    prompt_usuario = f"Por favor, simplifique o seguinte texto:\n\n{texto_complexo}"
    
    try:
        # Chamando o modelo local carregado no Ollama
        resposta = ollama.chat(
            model='qwen2.5:7b',
            messages=[
                {'role': 'system', 'content': prompt_sistema},
                {'role': 'user', 'content': prompt_usuario}
            ],
            options={
                'temperature': 0.3, # Menor temperatura para evitar alucinações e manter a fidelidade
            }
        )
        return resposta['message']['content']
        
    except Exception as e:
        return f"Erro ao conectar com o modelo local: {e}"

if __name__ == "__main__":
    # Exemplo de texto com alta densidade de termos complexos
    texto_para_teste = (
        "A inteligência artificial generativa denota avanços ímpares na cognição computacional, "
        "viabilizando a confecção de discursos textuais de elevada fidedignidade semântica."
    )
    
    print("--- Texto Original ---")
    print(texto_para_teste)
    print("\n--- Simplificação Realizada pelo Qwen 2.5 ---")
    
    texto_simplificado = simplificar_texto(texto_para_teste)
    print(texto_simplificado)
```

---

## 📊 Passo 3: O que avaliar após a execução?

Ao rodar esse teste na sua máquina, utilize as réguas que definimos na metodologia de avaliação para medir a qualidade do resultado:

1.  **Fidelidade Semântica (Inspirado no ASSIN2):** O texto simplificado manteve a mensagem original (de que as IAs criam textos muito bons e parecidos com o humano)? Ou inventou informações novas?
2.  **Seguimento de Instruções (Inspirado no CAPITU):** A IA respeitou as ordens de dividir as frases e evitar palavras rebuscadas?
3.  **Complexidade do Texto (Inspirado no NILC-Metrix):** As palavras utilizadas na resposta são mais comuns e fáceis de visualizar na mente do que as do texto original?

---
*Este guia faz parte do projeto de sistematização e avaliação de tecnologias de GenAI em português.*
