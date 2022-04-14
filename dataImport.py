import json
from pathlib import Path
import os
import random

class Word:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition

def nextWord():
    dataDir = Path.home() 
    filepath = os.path.join(dataDir, "definitionwordle/data/a.json")
    allWords = []

    with open(filepath) as json_file:
        data = json.load(json_file)
   
    for i in data:
        if ' ' not in i:
            wordAndDef = Word(i, data[i]["meanings"][0]["def"])
            allWords.append(wordAndDef)

    return allWords[random.randint(2,222)]
