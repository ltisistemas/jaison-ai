from src.domain.interfaces.voice_input import VoiceInputInterface
import speech_recognition as sr

class WhisperVoiceInput(VoiceInputInterface):
    def listen(self) -> str:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("🎤 Ouvindo...")
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_whisper_api(audio)
            print(f"🗣️ Você disse: {text}")
            return text
        except sr.UnknownValueError:
            print("❌ Não entendi o que você disse.")
            return ""
        except sr.RequestError as e:
            print(f"Erro na API do Whisper: {e}")
            return ""
