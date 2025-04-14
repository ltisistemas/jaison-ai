from models_llm.openrouter import LLMOpenRouter
from prepare import Prepare
from dotenv import dotenv_values, load_dotenv

class Main:
    def __init__(self):
        load_dotenv(dotenv_path=".env")
        self.config = dotenv_values(".env")
    
    def run(self):
        HISTORY = ""
        API_TOKEN = self.config["OPEN_ROUTER_AI"]
        BASE_URL = self.config["BASE_URL"]

        model = LLMOpenRouter(API_TOKEN, BASE_URL)

        prepare = Prepare(HISTORY)
        prepare.loop(model)

Main().run()

