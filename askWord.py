from dataImport import nextWord

wordObject = nextWord()
thisWord = wordObject.word
 

print(thisWord)
blockArr = []
wordArr = []
guessing = True
printed = False

for i in thisWord:
    blockArr.append(chr(9608))
    wordArr.append(i)
    
print(blockArr)

while guessing:
    guess = input("Guess a letter: ")
    s = thisWord
    c = guess
    lst = []

    for pos,char in enumerate(s):
        if(char == c):
            lst.append(pos)
    
    for i in lst:
        blockArr.pop(i)
        blockArr.insert(i, c)
        if len(lst) > 0 and printed == False:
            print(blockArr)
            #printed = True
        
        if chr(9608) not in blockArr:
            print("You won!")
            print("The definition of ",thisWord, "is:",wordObject.definition)
            guessing = False
     
