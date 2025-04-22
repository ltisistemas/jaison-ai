import pyttsx3

class Robo:
    def __init__(self):
        self.robo = pyttsx3.init()
        self.robo.setProperty('volume', 1)
        self.robo.setProperty('rate', 230)

    def falar(self, texto):
        self.robo.say(texto)
        self.robo.runAndWait()