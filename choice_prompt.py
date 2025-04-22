from InquirerPy import inquirer

from prompts import DEV_PROMPT, GENERAL_PROMPT, IMIGRACAO_PROMPT, STUDY_PROMPT
from messages import mensagens_boas_vindas

class ChoicePrompt:
    def select(self):
        choice = inquirer.select(
            message="Escolha a finalidade do Jaison-AI:",
            choices=[
                "👨‍💻 Desenvolvimento de Software",
                "🛂 Imigração para Portugal",
                "📚 Ajuda com estudos",
                "🧠 Assistente pessoal geral",
            ]

        ).execute()

        history = ""
        if choice == "👨‍💻 Desenvolvimento de Software":
            history = DEV_PROMPT, mensagens_boas_vindas.get("desenvolvimento")
        elif choice == "🛂 Imigração para Portugal":
            history = IMIGRACAO_PROMPT, mensagens_boas_vindas.get("imigracao")
        elif choice == "📚 Ajuda com estudos":
            history = STUDY_PROMPT, mensagens_boas_vindas.get("estudo")
        elif choice == "🧠 Assistente pessoal geral":
            history = GENERAL_PROMPT, mensagens_boas_vindas.get("geral")

        print(f"Você escolheu: {choice}")
        return history
