from dotenv import dotenv_values, load_dotenv
from rich.console import Console
from rich.markdown import Markdown
console = Console()

from dotenv import dotenv_values, load_dotenv
# Carrega API
load_dotenv(dotenv_path=".env")
config = dotenv_values(".env")

API_TOKEN = config["JAINSON_AI_KEY"]
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}

EXIT_COMMAND = "sair"
history = ""