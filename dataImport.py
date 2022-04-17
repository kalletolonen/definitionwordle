import json
from pathlib import Path
import os
from classes import Word

def nextWord():
    dataDir = os.getcwd()
    abc = "abcdefghijklmnopqrstuzyx"
    allWords = []

    for l in abc:
        filename = l
        filepath = os.path.join(dataDir,f"data/{filename}.json")
        
        with open(filepath) as json_file:
            data = json.load(json_file)
   
        for i in data:
            if ' ' not in i and '.' not in i and "'" not in i and len(i) == 5:
                wordAndDef = Word(i, data[i]["meanings"][0]["def"])
                allWords.append(wordAndDef)

    return allWords
