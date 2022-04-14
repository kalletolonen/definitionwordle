import json
from pathlib import Path
import os

dataDir = Path.home() 
filepath = os.path.join(dataDir, "definitionwordle/data/a.json")
allWords = []
#wordOfTheDay = []

with open(filepath) as json_file:
    data = json.load(json_file)
   
for i in data:
    if ' ' not in i:
        wordAndDef = {
            "word": i,
            "def": data[i]["meanings"][0]["def"]
            }
        allWords.append(wordAndDef)
print(allWords[990])
 
