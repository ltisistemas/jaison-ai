# Jaison AI 🤖

**Jaison AI** é um assistente pessoal inteligente que funciona por comandos de voz em um Raspberry Pi. Integrado com a API ChatGPT, responde perguntas e realiza tarefas de forma natural. O sistema possui design modular e eficiente dissipação de calor, sendo facilmente personalizável e expansível.

---

## 🚀 Características

- 🎤 Ativação por voz com o comando **"Olá, Jaison"**
- 🧠 Integração com **ChatGPT (OpenAI)**
- 🔊 Respostas por **síntese de voz**
- 🧱 Design modular com **caixa 3D impressa**
- 💨 Sistema de **resfriamento com ventilação e dissipadores**
- 🔁 Modo de escuta contínua (em desenvolvimento)

---

## 📦 Requisitos

- **Raspberry Pi 4** (ou superior)
- **Microfone USB** de boa qualidade
- **Caixa de som** compatível com o Pi
- **Python 3.7+**
- Conexão com a internet

---

## 🧰 Bibliotecas Utilizadas

```bash
pip install openai speechrecognition gTTS pyttsx3 openai python-dotenv
```

---

## ⚙️ Configuração

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/jaison-ai.git
cd jaison-ai
```

### 2. Configurar a chave da API OpenAI

Crie um arquivo `.env` com sua chave:

```env
OPENAI_API_KEY="sua_chave_aqui"
```

### 3. Conectar microfone e caixa de som

Verifique se os dispositivos estão funcionando corretamente com o Raspberry Pi.

### 4. Rodar o assistente

```bash
python main.py
```

---

## 💬 Como funciona

1. O Jaison AI escuta o ambiente aguardando o comando: **"Olá, Jaison"**
2. Ao detectar a ativação, inicia uma conversa por voz.
3. Envia a sua pergunta para o ChatGPT e responde com voz sintetizada.
4. Permanece em escuta até que a interação seja encerrada.

---

## 🛠️ Personalização

- **Frase de ativação** → Altere no código para o que quiser.
- **Voz do assistente** → Pode ser trocada por outras bibliotecas TTS.
- **Design físico** → A estrutura 3D pode ser personalizada conforme seu gosto.
- **Integração com APIs** → Adicione suporte a dispositivos IoT, calendários, e mais.

---

## 📈 Roadmap (em breve)

- [ ] Interface com visor LCD ou e-ink
- [ ] Modo escuta contínua com wake word detector otimizado
- [ ] Controle de dispositivos domésticos
- [ ] App mobile para controle remoto

---

## 🤝 Contribuições

Contribuições são muito bem-vindas! Faça um fork, crie uma branch com sua feature, e envie um pull request! 💡

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 📬 Contato

Dúvidas, sugestões ou ideias? Fale comigo:

- GitHub: [@seu-usuario](https://github.com/seu-usuario)
- E-mail: seu-email@dominio.com

---

Feito com 💙 e Python por **[Seu Nome]**
