from openai import OpenAI
from src.domain.interfaces.ai_output import AIOutputInterface

class OpenRouterOutput(AIOutputInterface):
    def __init__(self, api_token=None, api_url=None, model=None):
        self.__api_key = api_token or "SUA_CHAVE_AQUI"
        self.__api_url = api_url or "https://openrouter.ai/api/v1/chat/completions"
        self.__model = model or "gpt-3.5-turbo"
        self.__client = OpenAI(api_key=self.__api_key, base_url=self.__api_url)

    def generate_response(self, prompt: str) -> str:
        """
        Generates a response using the OpenRouter API.
        :param input: The input string to generate a response for.
        :return: The generated response string.
        """
        # Implement the API call to OpenRouter here
        completation = self.__client.chat.completions.create(
            model=self.__model,
            messages=[
                {
                "role": "user",
                "content": prompt
                }
            ]
        )

        if not completation.choices:
            raise ValueError("No choices returned from the API.")
        if not completation.choices[0].message:
            raise ValueError("No message returned from the API.")

        return completation.choices[0].message.content
