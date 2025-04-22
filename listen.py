import sounddevice as sd
import numpy as np
from rich.console import Console
from faster_whisper import WhisperModel
import torchaudio
import torch
from datetime import datetime
import os
from similar import Similar


class Listen:
    def __init__(self, similar=Similar, model_name=None):
        self.__console = Console()
        self.__model = model_name or WhisperModel("turbo", device="cpu", compute_type="int8")
        self.__samplerate = 16000
        self.__duracao = 3
        self.__similar = similar
    
    def __gravar(self):
        audio = sd.rec(int(self.__duracao * self.__samplerate), samplerate=self.__samplerate, channels=1, dtype='float32')
        sd.wait()

        if np.max(np.abs(audio)) < 1e-3:
            self.__console.print("[bold red]⚠️ Áudio muito silencioso! Verifique o microfone.[/bold red]")
            return None
        self.__console.print("[bold green]🎤 Audio capturado![/bold green]")
        tensor_audio = torch.from_numpy(audio.T)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        caminho_temp = f"audio_{timestamp}.wav"
        torchaudio.save(caminho_temp, tensor_audio, self.__samplerate)
        return caminho_temp

    def __transcrever(self, caminho_audio):
        segments, info = self.__model.transcribe(caminho_audio, language="pt")
        return " ".join([segment.text for segment in segments]).strip().lower()

    def esperar_ativacao(self):
        self.__console.print("[bold blue]👂 Aguardando 'Olá Jaison'...[/bold blue]")
        caminho = self.__gravar()
        if not caminho:
            return ""

        texto = self.__transcrever(caminho)
        os.remove(caminho)

        self.__similar.saida(texto)
        if (texto == ""):
            self.console.print("[bold red]🤖 Encerrando... até logo![/bold red]")
            return "[EXEC_EXIT]"

        self.__similar.ativacao(texto)
        if not texto or texto == "":
            self.__console.print("[bold red]❌ Nenhuma frase-chave detectada. Tente novamente.[/bold red]")
            return ""

        return texto

    def escutar_comando(self):
        self.__console.print("[bold green]🎧 Ouvindo comando contínuo...[/bold green]")
        caminho = self.__gravar()
        if not caminho:
            return ""

        texto = self.__transcrever(caminho)
        os.remove(caminho)

        self.__console.print(f"[bold cyan]🗣️ Texto capturado:[/bold cyan] {texto}")
        return texto
