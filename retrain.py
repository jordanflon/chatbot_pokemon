import os
from os import listdir
from os.path import isfile, join

to_keep=["README.txt", "intents.json", "main.py", "retrain.py","pokemon.txt","scrapping.py", "display.py", "chatbot_discord.py","main2_chatbot.py" ,"chatbot_messenger"]

path = os.getcwd()
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

for i in range(len(onlyfiles)) :
    if onlyfiles[i] not in to_keep:
        os.remove(onlyfiles[i])

print("Launch main.py now")
