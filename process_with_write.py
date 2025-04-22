from interfaces.contract_process import ContractProcess
from messages import EXIT_MESSAGE, FIRST_MESSAGE, NEXT_MESSAGES, SYSTEM_PROMPT
from models_llm.contract_llm import LLMContractInterface
from rich.console import Console
from robo import Robo
from similar import Similar


class ProcessWithWrite(ContractProcess):
    def __init__(self, llm: LLMContractInterface, console: Console, similar: Similar, history: str, first_message: str):
        self.__llm = llm
        self.__console = console
        self.__similar = similar
        self.__history = history
        self.__first_message = first_message

    def check_exit(self, input):
        texto = input.lower()
        self.__similar.saida(texto)
        
        return texto != ""
    
    def get_response(self, input):
        self.__history += f"\n[USER]: {input}"
        self.__console.print(f"[bold blue]R: {input}[/bold blue]")
        
        response = self.__llm.get_response(self.__history)
        self.__history += f"\n[ASSISTANT]: {response}"
        
        return response

    def execute(self):
        input = self.__console.input(self.__first_message, markup=True)

        while True:
            if (self.check_exit(input)):
                self.__console.print(EXIT_MESSAGE)
                break
            
            response = self.__llm.generate_response(input)
            self.__history += f"\nUsuário: {self.user_input}\nAssistente: {response}"
            input = self.__console.input(NEXT_MESSAGES)
