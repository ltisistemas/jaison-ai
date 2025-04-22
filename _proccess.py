from rich.console import Console
from listen import Listen
from messages import FIRST_MESSAGE_ROBO
from models_llm.contract_llm import LLMContractInterface
from robo import Robo
from similar import Similar

class Proccess:
    def __init__(self, listen: Listen, llm: LLMContractInterface, console: Console, similar: Similar, robo=Robo):
        self__llm = llm
        self.__console = console
        self.__history = ""
        self.__listen = listen
        self.__similar = similar
        self.__robo = robo

    def execute(self):
        while True:
            texto = self.__listen.escutar_comando()
            if not texto or texto == "":
                self.__console.print("[bold red]❌ Nenhuma frase-chave detectada. Tente novamente.[/bold red] Fale sair para encerrar.")
                return True
            
            if texto == "[EXEC_EXIT]": break
            self.__robo.falar(FIRST_MESSAGE_ROBO)

