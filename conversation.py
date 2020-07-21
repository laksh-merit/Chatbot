import os
import aiml
import pyttsx3
#from autocorrect import spell

engine = pyttsx3.init()

BRAIN_FILE="./pretrained_model/aiml_pretrained_model.dump"

k = aiml.Kernel()

if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="./pretrained_model/learningFileList.aiml", commands="load aiml")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)


while True:
    query = input("User > ")
    #query = [spell(w) for w in (query.split())]
    #question = " ".join(query)
    response = k.respond(query)
    if response:
        print("bot > ", response)
        engine.say(response)
        engine.runAndWait()
    else:
        print("bot > :) ", )
