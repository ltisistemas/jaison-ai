class LLMContractInterface:
    def generate_response(self, input):
        raise NotImplementedError("Subclasses should implement this method")