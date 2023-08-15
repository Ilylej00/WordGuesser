import random as randy

# takes a filename/path, returns a list
# of all lines of the file that are exactly 5
# characters long (ignoring newlines)
def read5LetterWords(fileName):
    fileVar = open(fileName)
    result = []
    for line in fileVar:
        word = str.strip(fileVar.readline())
        if (len(word) == 5):
            result.append(word)
    fileVar.close()
    return result

words = read5LetterWords("words.csv")
randIndex = randy.randint(0, len(words) - 1)
word = words[randIndex]

userGuess = ""
correctLetters = set()

# checks the guess word against the word to be guessed
# returns a string of length 5 where every letter
# that matches the real word positionally is present
# and the rest of the letters are '*'
def checkGuess(guess, real):
    # reject guesses that are not 5 letters long
    if (len(guess) != 5):
        print("word must be 5 letters long")
        return ""
    
    output = ""
    for i in range(5):
        if (guess[i] in real):
            correctLetters.add(guess[i])
        if (guess[i] == real[i]):
            output += real[i]
        else:
            output += "*"
    return output

print("\n\n##############################################################")
print("Welcome to billy's wordl!")
print("make sure you only guess 5 letter words,")
print("if you can't guess the word, type \"end!\" to give up")
print("##############################################################\n")

while (userGuess != "end!" and userGuess != word):
    userGuess = input("type your guess: ")
    print(checkGuess(userGuess, word))
    print("Correct letters: " + str(correctLetters) + "\n")
if (userGuess != word):
    print("The word was: " + word + "!")
else:
    print("good job! you got it!")