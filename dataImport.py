import json
from pathlib import Path
import os
import random
from classes import Word

def nextWord():
    dataDir = Path.home() 
    filepath = os.path.join(dataDir, "definitionwordle/data/a.json")
    allWords = []

    with open(filepath) as json_file:
        data = json.load(json_file)
   
    for i in data:
        if ' ' not in i and '.' not in i and len(i) == 5:
            wordAndDef = Word(i, data[i]["meanings"][0]["def"])
            allWords.append(wordAndDef)

    return allWords
