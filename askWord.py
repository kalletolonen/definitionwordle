from dataImport import nextWord
from score import *
import random
from printScore import *

def checker(guess, thisWord, wordArr, wrongLetters):
    guessArr = []
    win = False
    for l in guess:
        guessArr.append(l)
        index = guess.find(l)
        if guess.find(l) != thisWord.find(l) and l in thisWord:
            guessArr.pop(index)
            guessArr.insert(index, f"{l}*")
        elif guess.find(l) == thisWord.find(l):
            guessArr.pop(index)
            guessArr.insert(index, l.upper())
        else:
            wrongLetters.append(l)
    if guessArr == wordArr:
        win = True
    return guessArr, win, wrongLetters


mydictionary = nextWord()
wordObject = mydictionary[random.randint(0, len(mydictionary))]
thisWord = wordObject.word
#print(thisWord)  # for testing
justWords = []

for i in range(0, len(mydictionary)):
    justWords.append(mydictionary[i].word.lower())

winArr = []
prevGuesses = []
wordArr = []
wrongLetters = []
guessing = True
playerQuit = False
guesses = 1
maxGuesses = 7
noPrint = False
win = False

for i in thisWord:
    wordArr.append(i.upper())

while guessing and guesses < maxGuesses:
    guess = input(f"Guess ({guesses}/{maxGuesses - 1}) the word (q quits): ")
    guess = guess.lower()

    if guess == "q":
        guessing = False
        playerQuit = True
    if len(guess) == len(wordArr) and guess in justWords:
        letters = guess
        guesses = guesses + 1
        print("Right letter, right place = CAPS\nRight letter, wrong place = *")
        guessArr, win, wrongLetters = checker(guess, thisWord, wordArr, wrongLetters)
        prevGuesses.append(guessArr)
        if wrongLetters != "None":
            print("Not in the word:\n ",wrongLetters)
        for i in prevGuesses:
                    print(i)
    elif guess not in justWords:
        if len(guess) == len(wordArr):
            print("Not in dictionary!")
        elif guess != "q":
            print("You word is not the right lenght.")

    if win:
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
