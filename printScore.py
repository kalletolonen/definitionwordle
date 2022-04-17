import csv

def printScore():
    with open('scores.csv', newline='') as score:
        scoreReader = csv.reader(score)
        for points in scoreReader:
            print(f"Guesses: {points}")
