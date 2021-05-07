import random

responses = ["Yes", "No", "Ask again"]

while True:
    ask = input("\n\nAsk a qustion > ")
    print (random.choice(responses))
    