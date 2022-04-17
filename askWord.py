from dataImport import nextWord
from score import *
import random
from printScore import *

def checker(guess, thisWord):
    guessArr = []
    for l in guess:
        guessArr.append(l)
        if guess.find(l) != thisWord.find(l) and l in thisWord:
            index = guess.find(l)
            guessArr.pop(index)
            guessArr.insert(index, l.upper())
    return guessArr


mydictionary = nextWord()
wordObject = mydictionary[random.randint(0, len(mydictionary))]
thisWord = wordObject.word
print(thisWord)  # for testing
justWords = []

for i in range(0, len(mydictionary)):
    justWords.append(mydictionary[i].word.lower())

blockArr = []
wordArr = []
guessing = True
playerQuit = False
guesses = 1
maxGuesses = 7
noPrint = False
testing = True

for i in thisWord:
    blockArr.append(chr(9608))
    wordArr.append(i)
print(blockArr)

while guessing and guesses < maxGuesses:
    print(f"Guess: {guesses}/{maxGuesses - 1}")
    guess = input("\nGuess the word (q quits): ")
    guess = guess.lower()

    if guess == "q":
        guessing = False
        playerQuit = True
    if len(guess) == len(wordArr) and guess in justWords:
        letters = guess
        guesses = guesses + 1
        for num, letter in enumerate(letters, start=0):
            if wordArr[num] == letter:
                blockArr.pop(num)
                blockArr.insert(num, letter)
        print("The correct letters on wrong indexes are on CAPS\n", checker(guess, thisWord))
        print("Correct letters in right indexes:\n",blockArr)
    elif guess not in justWords:
        if len(guess) == len(wordArr):
            print("Not in dictionary!")
        elif guess != "q":
            print("You word is not the right lenght.")

    if chr(9608) not in blockArr:
        winner(guesses-1)
        stats(thisWord,guesses-1)
        print("The definition of", thisWord, "is:", wordObject.definition)
        guessing = False
        noPrint = True

if noPrint == False and playerQuit and guesses >= 2:
    guesses = 7
    stats(thisWord,guesses)
    print(f"The correct word was: {thisWord} \nDefinition: {wordObject.definition}")
elif playerQuit:
    print(f"The correct word was: {thisWord} \nDefinition: {wordObject.definition}")

try:
    print('\n')
    printScore()
except:
    print("No scores yet :/")

