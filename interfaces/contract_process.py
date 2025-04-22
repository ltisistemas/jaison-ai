class ContractProcess:
    def execute(self):
        raise NotImplementedError("Subclasses should implement this method.")
    
    def get_response(self, input):
        raise NotImplementedError("Subclasses should implement this method.")
    
    def get_history(self):
        raise NotImplementedError("Subclasses should implement this method.")
    
    def set_history(self, history):
        raise NotImplementedError("Subclasses should implement this method.")