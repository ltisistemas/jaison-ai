from domain.interfaces.ai_output import AIOutputInterface


class AiOutputInteraction:
    def __init__(self, ai_output: AIOutputInterface):
        self.__ai_output = ai_output

    def run(self, prompt: str) -> str:
        response = self.ai_output.generate_response(prompt)
        return response