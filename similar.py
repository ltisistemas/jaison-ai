from rapidfuzz import fuzz

class Similar:
    def __init__(self):
        self.__frases_chave = ["olá jaison", "e aí jaison", "acorda jaison", "oi jason", "olá, jason"]
        self.__frases_sair = ["sair", "encerrar", "desligar", "desconectar", "tchau jaison", "tchau jason", "tchau", "desligar jaison", "desligar jason"]

    def ativacao(self, texto):
        for k in self.__frases_chave:
            if fuzz.partial_ratio(texto, self.__frases_chave) > 85:
                return texto
            
        return ""

    def saida(self, texto):
        for k in self.__frases_chave:
            if fuzz.partial_ratio(texto, self.__frases_sair) > 85:
                return texto
            
        return ""