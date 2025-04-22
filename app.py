# from listen import Listen
# from _proccess import Proccess
# from robo import Robo
from dotenv import dotenv_values, load_dotenv
from rich.console import Console

from choice_prompt import ChoicePrompt
from models_llm.openrouter import LLMOpenRouter
from process_with_write import ProcessWithWrite
from similar import Similar

class App:
    def __init__(self):
        load_dotenv(dotenv_path=".env")
        self.__config = dotenv_values(".env")
        self.__console = Console()
        self.__console.print("[bold yellow]Iniciando o assistente...[/bold yellow]")
    
    def run(self):
        # HISTORY = ""
        API_TOKEN = self.__config["OPEN_ROUTER_AI"]
        BASE_URL = self.__config["BASE_URL"]

        similar = Similar()
        model = LLMOpenRouter(API_TOKEN, BASE_URL)
        # listen = Listen(similar=similar)
        # robo = Robo()

        choice = ChoicePrompt()
        history, first_message = choice.select()

        # process = Proccess(listen, model, self.__console, similar, robo)
        process = ProcessWithWrite(llm=model, console=self.__console, similar=similar, history=history, first_message=first_message)
        process.execute()