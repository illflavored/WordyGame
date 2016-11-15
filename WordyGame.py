import string
import random
import csv
import sys

# Initialize the List
letterList = []

# Create our list of random letters
def createLetters(numLetters):   
    for x in range(0, numLetters):
        #tempLetter = random.choice('abcdefghijklmnopqrstuvwxyz')
        tempLetter = random.choice('abcdefghijklmnopqrstuvwxyz')
        letterList.append(tempLetter)

createLetters(15)

print("Your list of letters is:")
print(letterList)
print("")

# Ask for user input for a word
wordGuess = input('Enter a word: ')

print(("Your guess was " + wordGuess.upper()))

print("")
print(list(wordGuess))
listedWord = list(wordGuess)

print(set(letterList) & set(wordGuess))

# Checks to see if those letters exist in our list
if set(listedWord) <= set(letterList):
    print(("The letters for the word " + wordGuess.upper() + " exist in our letter list. Good job."))
else:
    print(("The letters for the word " + wordGuess.upper() + " aren't in our letter list. Bad guess."))

# Check to see if the guess is an actual word

tempDict = open('/Users/msveen/Python/WordyWords/short.txt', 'r')
dictionary = tempDict.readlines()

print(set(wordGuess) & set(dictionary))

#if set(listedWord) <= set(letterList):
#    print(("The letters for the word " + wordGuess.upper() + " exist in our letter list. Good job."))
#else:
#    print(("The letters for the word " + wordGuess.upper() + " aren't in our letter list. Bad guess."))

# If it does, award points and replace those letters
        
