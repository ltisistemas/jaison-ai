from src.core.entities.assistant import Assistant
from src.adapters.input.voice_input import VoiceInputInterface
from src.interfaces.contract_llm import LLMContractInterface

class VoiceInteraction:
    def __init__(self, assistant: Assistant, voice_input: VoiceInputInterface, llm: LLMContractInterface):
        self.assistant = assistant
        self.voice_input = voice_input
        self.output = llm

    def process_voice_command(self):
        # Captura o comando de voz
        command = self.voice_input.capture_command()
        
        if command:
            # Processa o comando com a resposta do OpenRouter
            response = self.output.generate_response(command)
            return response
        else:
            return "Desculpe, não consegui entender seu comando."

    def __str__(self):
        return f"Voice Interaction with {self.assistant.name} ({self.assistant.version})"
