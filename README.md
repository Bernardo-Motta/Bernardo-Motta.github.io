# 🤖 Avaliação & Sistematização de GenAI

Bem-vindo ao repositório de sistematização e avaliação de tecnologias de Inteligência Artificial Generativa com foco no português brasileiro [5]. Aqui você encontrará análises de arquiteturas, guias de implementação e scripts prontos para rodar localmente [5].

---

## 🎯 Objetivo do Projeto
Centralizar e estruturar o conhecimento sobre modelos de linguagem (LLMs/SLMs) e sistemas agênticos, fornecendo um espaço limpo e de rápido acesso para desenvolvedores, pesquisadores e entusiastas testarem soluções locais [5].

---

## 📂 Organização da Base de Conhecimento

├── 🧠 Modelos (LLMs & SLMs)  --> Avaliação de modelos comerciais e locais ├── 🧩 Arquiteturas           --> Padrões de agentes (Single/Multi-Agent) ├── 📊 Métricas de Avaliação  --> Como medir legibilidade, custos e precisão └── 💻 Códigos & Testes       --> Scripts prontos para execução local

---

## 🧠 1. Modelos Analisados

| Modelo | Tipo | Foco Linguístico | Execução Local |
| :--- | :--- | :--- | :--- |
| **Sabiá-3** | LLM Comercial | Nativo em PT-BR | Não (Via API) |
| **Llama 3 (8B)** | SLM Aberto | Multilíngue | Sim (Quantizado) |
| **Qwen 2.5 (7B)** | SLM Aberto | Multilíngue | Sim (Quantizado) |

---

## 🧩 2. Arquiteturas de Agentes

Documentamos o comportamento e o fluxo de trabalho das principais arquiteturas:
*   **Single-Agent:** IAs projetadas para executar uma tarefa em loop (pensar, agir, observar).
*   **Sistemas Multiagentes:**
    *   *Padrão Supervisor:* Um agente central delega e avalia o trabalho de sub-agentes.
    *   *Padrão Swarm:* Colaboração dinâmica e descentralizada entre agentes especializados.

---

## 📊 3. Métricas e Avaliação

Nossas avaliações são baseadas em padrões rigorosos de qualidade:
1.  **Fidelidade e Sentido (ASSIN2):** Garantia de que a reescrita ou simplificação mantém a mensagem original íntegra.
2.  **Facilidade de Leitura (NILC-Metrix):** Análise do esforço cognitivo do leitor por meio de fórmulas de complexidade sintática.
3.  **Seguimento de Instruções (CAPITU):** Testes para garantir que a IA obedece a regras rígidas de formatação e limites.

---

## 💻 4. Códigos para Testes Locais

Acesse nossa pasta de [códigos e testes](./codes) para encontrar scripts prontos para rodar modelos locais quantizados utilizando frameworks como **Ollama** e **Python**.

*   [🤖 Como rodar o Qwen localmente](artigos/guia-qwen-local.md)
*   [🧩 Arquiteturas Multiagentes](artigos/arquiteturas-multiagentes.md)
*   [📊 Métricas de Legibilidade](artigos/metricas-legibilidade.md)

> 💡 **Quer contribuir?** Sinta-se à vontade para enviar um Pull Request com novos modelos ou scripts de teste!
