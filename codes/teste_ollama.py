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
