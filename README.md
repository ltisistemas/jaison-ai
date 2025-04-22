# Jaison AI 🤖

Jaison AI é um assistente pessoal inteligente, criado para rodar em um Raspberry Pi. Ele integra a API do ChatGPT e permite interações por voz, proporcionando respostas inteligentes e naturais, com foco em uma experiência de usuário fluida e eficiente.

## 🚀 Funcionalidades

- **Comandos de voz**: O Jaison AI escuta e responde a comandos de voz, realizando tarefas de acordo com as solicitações.
- **Integração com ChatGPT**: O assistente utiliza a API do ChatGPT para oferecer respostas contextuais e inteligentes.
- **Personalização**: A arquitetura modular do sistema permite que você ajuste e adicione novas funcionalidades facilmente.
- **Performance otimizada**: O projeto foi desenvolvido para ser eficiente, com foco em baixo custo e boa performance em dispositivos como o Raspberry Pi.

## 🔧 Instalação

### Pré-requisitos

- **Python 3.7+**: Certifique-se de ter o Python instalado na sua máquina.
- **Raspberry Pi** ou outro sistema de baixo custo.
- **Chave da API do ChatGPT**: Você precisará de uma chave válida para interagir com o ChatGPT.

### Passos

1. Clone o repositório para sua máquina local:

   ```bash
   git clone https://github.com/ltisistemas/jaison-ai.git
   cd jaison-ai
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure as variáveis de ambiente necessárias, como a chave de API do ChatGPT:

   - Crie um arquivo `.env` com o seguinte conteúdo:

   ```bash
   CHATGPT_API_KEY=your_api_key_here
   ```

4. Execute o assistente:

   ```bash
   python main.py
   ```

## 📝 Estrutura do Repositório

- **`main.py`**: Ponto de entrada para iniciar o assistente.
- **`app.py`**: Script responsável por configurar e iniciar o sistema.
- **`listen.py`**: Responsável por captar e processar os comandos de voz.
- **`prompts.py`**: Define os prompts utilizados para interagir com a API do ChatGPT.

## 🛠 Contribuições

Contribuições são bem-vindas! Se você tiver ideias ou melhorias para o projeto, basta abrir uma **issue** ou enviar um **pull request**. Sinta-se à vontade para fazer modificações, desde que siga as melhores práticas de codificação.

## 📜 Licença

Este projeto é licenciado sob a licença **MIT**. Consulte o arquivo [LICENSE](LICENSE) para mais informações.
