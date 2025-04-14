from dotenv import dotenv_values, load_dotenv
from rich.console import Console
from rich.markdown import Markdown
console = Console()

from dotenv import dotenv_values, load_dotenv
# Carrega API
load_dotenv(dotenv_path=".env")
config = dotenv_values(".env")

API_TOKEN = config["OPEN_ROUTER_AI"]
BASE_URL = config["BASE_URL"]
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}

from openai import OpenAI
client = OpenAI(api_key=API_TOKEN,base_url=BASE_URL)
completation = client.chat.completions.create(
    model="openai/gpt-40",
    messages=[
        {
        "role": "user",
        "content": "What is the meaning of life?"
        }
    ]
)

EXIT_COMMAND = "sair"
history = ""