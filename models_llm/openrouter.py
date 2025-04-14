from openai import OpenAI

from models_llm.contract_llm import LLMContractInterface

class LLMOpenRouter(LLMContractInterface):
    def __init__(self, api_key, base_url, model="gpt-3.5-turbo"):
        self.api_key = api_key
        self.base_url = base_url
        self.model = model
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)

    def generate_response(self, input):
        """
        Generates a response using the OpenRouter API.
        :param input: The input string to generate a response for.
        :return: The generated response string.
        """
        # Implement the API call to OpenRouter here
        completation = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                "role": "user",
                "content": input
                }
            ]
        )

        if not completation.choices:
            raise ValueError("No choices returned from the API.")
        if not completation.choices[0].message:
            raise ValueError("No message returned from the API.")

        return completation.choices[0].message.content
        