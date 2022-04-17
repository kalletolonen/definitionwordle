import json
from pathlib import Path
import os
import random
from classes import Word

def nextWord():
    dataDir = Path.home() 
    abc = "abcdefghijklmnopqrstuzyx"
    #filename = "a"
    #filepath = os.path.join(dataDir,f"definitionwordle/data/{filename}.json")
    allWords = []

    for l in abc:
        filename = l
        filepath = os.path.join(dataDir,f"definitionwordle/data/{filename}.json")
        
        with open(filepath) as json_file:
            data = json.load(json_file)
   
        for i in data:
            if ' ' not in i and '.' not in i and "'" not in i and len(i) == 5:
                wordAndDef = Word(i, data[i]["meanings"][0]["def"])
                allWords.append(wordAndDef)

    return allWords
