from doorkeeper import Doorkeeper
from conversation import Conversation
from jsongeneration import JSONGeneration, reset_count

def Main(prompt):
    
    if (Doorkeeper(prompt) == "0"):
        return Conversation(prompt)
    elif (Doorkeeper(prompt) == "1"):
        return JSONGeneration(prompt)