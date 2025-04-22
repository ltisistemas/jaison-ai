from application.usecases.ai_output_interaction import AiOutputInteraction
from messages import EXIT_MESSAGE, NEXT_MESSAGES
from similar import Similar
from rich.console import Console

class InteractionController:
    def __init__(self, use_case: AiOutputInteraction, similar: Similar, console: Console, history: str):
        self.__use_case = use_case
        self.__similar = similar
        self.__history = history
        self.__console = console


    def check_exit(self, input):
        texto = input.lower()
        self.__similar.saida(texto)
        
        return texto != ""

    def execute(self):
        input = self.__console.input(self.__first_message, markup=True)

        while True:
            if (self.check_exit(input)):
                self.__console.print(EXIT_MESSAGE)
                break
            
            response = self.__use_case.run(input)
            # self.__llm.generate_response(input)
            self.__history += f"\nUsuário: {self.user_input}\nAssistente: {response}"
            input = self.__console.input(NEXT_MESSAGES)
