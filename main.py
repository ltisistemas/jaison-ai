from config import console, history
import functions
from messagens import FIRST_MESSAGE, NEXT_MESSAGES,SYSTEM_PROMPT

user_input = console.input(FIRST_MESSAGE)
history += SYSTEM_PROMPT

while functions.submit(user_input):
    user_input = console.input(NEXT_MESSAGES)
    