from dataImport import nextWord

wordObject = nextWord()
thisWord = wordObject.word

print(thisWord)
blockArr = []
wordArr = []
guessArr = []
guessing = True

for i in thisWord:
    blockArr.append(chr(9608))
    wordArr.append(i)
    
while guessing:
    print(blockArr)
    guess = input("Guess the word: ")

    letters = guess
    for num, letter in enumerate(letters, start=0):
        if wordArr[num] == letter:
            blockArr.pop(num)
            blockArr.insert(num, letter)
        
    if chr(9608) not in blockArr:
       print("You won!")
       print("The definition of ",thisWord, "is:",wordObject.definition)
       guessing = False
     
