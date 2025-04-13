
import requests
import pyttsx3
import speech_recognition as sr
from dotenv import dotenv_values, load_dotenv
from rich.console import Console

console = Console()

# Inicializa TTS
robo = pyttsx3.init()
robo.setProperty('volume', 1)
robo.setProperty('rate', 160)
voices = robo.getProperty('voices')
robo.setProperty('voice', voices[0].id)  # Ajuste se quiser voz feminina

# Inicializa reconhecimento de fala
r = sr.Recognizer()

# Carrega API
load_dotenv(dotenv_path=".env")
config = dotenv_values(".env")

API_TOKEN = config["HUGGIN_FACE_API_KEY"]
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}

EXIT_COMMAND = "sair"
history = ""

def gerar_prompt(user_input):
    return (
        history
        + f"\nUsuário: {user_input}"
        + "\nJaison (responda com simpatia, linguagem acessível, e como um amigo explicando com clareza):"
    )

def escutar_comando(timeout=5):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        console.print("[bold yellow]👂 Aguardando 'Olá Jaison'...[/bold yellow]")
        try:
            audio = r.listen(source, timeout=timeout)
            comando = r.recognize_google(audio, language="pt-BR").lower()
            return comando
        except (sr.UnknownValueError, sr.WaitTimeoutError):
            return ""
        except sr.RequestError as e:
            console.print(f"[bold red]Erro de reconhecimento de voz: {e}[/bold red]")
            return ""

def falar(texto):
    robo.say(texto)
    robo.runAndWait()

# Loop principal
while True:
    ativado = False
    while not ativado:
        comando = escutar_comando(timeout=5)
        if "olá jaison" in comando:
            ativado = True
            console.print("[bold cyan]🤖 Oi! Estou te ouvindo. Pode perguntar.[/bold cyan]")
            falar("Oi! Estou te ouvindo. Pode perguntar.")
        elif comando == EXIT_COMMAND:
            console.print("[bold red]Encerrando... até logo![/bold red]")
            falar("Encerrando. Até logo!")
            exit()

    # Após ativação, escuta pergunta do usuário
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        console.print("[bold cyan]🎤 Pode falar sua pergunta...[/bold cyan]")
        try:
            audio = r.listen(source, timeout=10)
            user_input = r.recognize_google(audio, language="pt-BR")
        except sr.WaitTimeoutError:
            console.print("[bold red]⏰ Tempo esgotado. Nenhuma pergunta detectada.[/bold red]")
            falar("Não ouvi nenhuma pergunta. Pode tentar novamente.")
            continue
        except sr.UnknownValueError:
            console.print("[bold red]❌ Não entendi o que você disse.[/bold red]")
            falar("Desculpe, não entendi. Pode repetir?")
            continue

    if user_input.lower() == EXIT_COMMAND:
        console.print("[bold red]Encerrando... até logo![/bold red]")
        falar("Encerrando. Até logo!")
        break

    # Gera resposta com o modelo
    prompt = gerar_prompt(user_input)
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 512,
            "return_full_text": False,
            "temperature": 0.7
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code != 200:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")

    answer = response.json()[0].get("generated_text", "").strip()
    console.print(f"[bold green]{answer}[/bold green]")
    falar(answer)

    # Atualiza histórico
    history += f"\nUsuário: {user_input}\nAssistente: {answer}"
