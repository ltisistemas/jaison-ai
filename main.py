from src.application.controllers.interaction_controller import InteractionController
from src.application.usecases.voice_interaction import VoiceInteractionUseCase
from src.infra.factories.ai_output_factory import create_ai_output
from src.infra.factories.voice_input_factory import create_voice_input


def main():
    voice_input = create_voice_input()
    ai_output = create_ai_output()
    
    use_case = VoiceInteractionUseCase(voice_input, ai_output)
    controller = InteractionController(use_case)
    
    controller.execute()

if __name__ == "__main__":
    main()
