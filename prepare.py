from messages import EXIT_COMMAND, FIRST_MESSAGE, NEXT_MESSAGES, SYSTEM_PROMPT
from rich.console import Console

from models_llm.contract_llm import LLMContractInterface

class Prepare:
    def __init__(self,history):
        self.console = Console()
        self.history = history
        self.history += SYSTEM_PROMPT

    def verifica_sair(self):
        if (self.user_input.lower() == EXIT_COMMAND):
            self.console.print("[bold red]🤖 Encerrando... até logo![/bold red]")
            return False
        return True

    def loop(self, llm: LLMContractInterface):
        self.user_input = self.console.input(FIRST_MESSAGE)
        
        while True:
            # Verifica se o usuário deseja sair
            if not self.verifica_sair(): break

            try:
                # Solicita a resposta da IA e imprime pro usuário
                response = llm.generate_response(self.user_input)
                self.console.print(f"[bold green]🤖 Resposta: {response}[/bold green]")

                # Atualiza histórico
                self.history += f"\nUsuário: {self.user_input}\nAssistente: {response}"
                
                # Inicia o fluxo novamente
                self.user_input = self.console.input(NEXT_MESSAGES)
            except Exception as e:
                self.console.print(f"[bold red]🤖 Erro: {e}[/bold red]")
                break



