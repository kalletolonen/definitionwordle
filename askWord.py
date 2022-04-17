from dataImport import nextWord
import random

#def checker(guess, thisWord):
#    for l in guess:
#        if thisWord.count(l) <= guess.count(l):
#            print(l,"is in the word (but not @ right index): ",thisWord.count(l))

def checker(guess, thisWord):
    for l in guess:
        if guess.find(l) == thisWord.find(l):
        	print(f"The letter {l} is in the right place")
        if guess.find(l) < thisWord.find(l) and l in thisWord:
        	print(f"The letter {l} is in the word, but at a bigger index")
        if guess.find(l) > thisWord.find(l) and l in thisWord:
                	print(f"The letter {l} is in the word, but at a smaller index")
        
        	
mydictionary = nextWord()
wordObject = mydictionary[random.randint(0,len(mydictionary))]
thisWord = wordObject.word
print(thisWord) #for testing
justWords = []

for i in range (0, len(mydictionary)):
    justWords.append(mydictionary[i].word.lower())

blockArr = []
wordArr = []
guessArr = []
guessing = True
guesses = 1
maxGuesses = 7
noPrint = False
testing = True

for i in thisWord:
    blockArr.append(chr(9608))
    wordArr.append(i)
    
while guessing and guesses < maxGuesses:
    print(f"Guess: {guesses}/{maxGuesses - 1}")
    print(blockArr)
    guess = input("\nGuess the word (q quits): ")
    guess = guess.lower()
    
    if guess == "q":
        guessing = False
    if len(guess) == len(wordArr) and guess in justWords:
        letters = guess
        guesses = guesses + 1
        for num, letter in enumerate(letters, start=0):
            if wordArr[num] == letter:
                blockArr.pop(num)
                blockArr.insert(num, letter)
        checker(guess,thisWord)
    elif guess not in justWords:
        if len(guess) == len(wordArr):
            print("Not in dictionary!")
        elif guess != "q":
            print("You word is not the right lenght.")

    if chr(9608) not in blockArr:
        print("You won!")
        print("The definition of",thisWord, "is:",wordObject.definition)
        guessing = False
        noPrint = True

if noPrint == False:
    print(f"The correct word was: {thisWord} \nDefinition: {wordObject.definition}")        
     
