import requests
import config

def prepare(user_input):
    return (
        config.history
        + f"\nUsuário: {user_input}"
        + "\nJaison (responda com simpatia, linguagem acessível, e como um amigo explicando com clareza):"
    )

def get_answer(user_input):
    prompt = prepare(user_input)
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 1024,
            "return_full_text": False,
            "temperature": 0.7
        }
    }
    response = requests.post(config.API_URL, headers=config.HEADERS, json=payload)
    if response.status_code != 200:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")

    answer = response.json()[0].get("generated_text", "").strip()
    return answer

def submit(user_input):
    if (user_input == config.EXIT_COMMAND):
        config.console.print("[bold red]Encerrando... até logo![/bold red]")
        return False
    else:
        try:
            answer = get_answer(user_input)
            config.history += f"\nUsuário: {user_input}\nAssistente: {answer}"
            config.console.clear()
            config.console.print(answer)
        except Exception as e:
            config.console.print(f"[bold red]Erro ao processar a solicitação:[/bold red] {e}")
        return answer