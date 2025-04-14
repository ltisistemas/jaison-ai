import config
import functions
from messagens import FIRST_MESSAGE, NEXT_MESSAGES,SYSTEM_PROMPT

user_input = config.console.input(FIRST_MESSAGE)
config.history = SYSTEM_PROMPT

while functions.submit(user_input):
    user_input = config.console.input(NEXT_MESSAGES)
    