import unittest
from unittest.mock import patch, MagicMock
from main import gerar_prompt, escutar_comando, falar

class TestMain(unittest.TestCase):

    def test_gerar_prompt(self):
        # Testa se o prompt é gerado corretamente
        global history
        history = "Histórico anterior"
        user_input = "Qual é a previsão do tempo?"
        expected_prompt = (
            "Histórico anterior\n"
            "Usuário: Qual é a previsão do tempo?\n"
            "Jaison (responda com simpatia, linguagem acessível, e como um amigo explicando com clareza):"
        )
        self.assertEqual(gerar_prompt(user_input), expected_prompt)

    @patch('main.sr.Microphone')
    @patch('main.sr.Recognizer')
    def test_escutar_comando(self, mock_recognizer, mock_microphone):
        # Testa se o comando é ouvido corretamente
        mock_instance = mock_recognizer.return_value
        mock_instance.listen.return_value = "audio_data"
        mock_instance.recognize_google.return_value = "olá jaison"

        comando = escutar_comando()
        self.assertEqual(comando, "olá jaison")
        mock_instance.recognize_google.assert_called_once_with("audio_data", language="pt-BR")

    @patch('main.pyttsx3.init')
    def test_falar(self, mock_pyttsx3):
        # Testa se o texto é falado corretamente
        mock_engine = MagicMock()
        mock_pyttsx3.return_value = mock_engine

        falar("Teste de fala")
        mock_engine.say.assert_called_once_with("Teste de fala")
        mock_engine.runAndWait.assert_called_once()

if __name__ == '__main__':
    unittest.main()