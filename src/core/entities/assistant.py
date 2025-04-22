class Assistant:
    def __init__(self, name: str, version: str, language: str):
        self.name = name
        self.version = version
        self.language = language

    def __str__(self):
        return f"Assistant {self.name}, Version {self.version}, Language {self.language}"
