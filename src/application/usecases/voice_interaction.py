from src.domain.interfaces.voice_input import VoiceInputInterface
from src.domain.interfaces.ai_output import AIOutputInterface

class VoiceInteractionUseCase:
    def __init__(self, voice_input: VoiceInputInterface, ai_output: AIOutputInterface):
        self.voice_input = voice_input
        self.ai_output = ai_output

    def run(self) -> str:
        prompt = self.voice_input.listen()
        response = self.ai_output.generate_response(prompt)
        return response
