secretWord = "Mission"
guess = ""
guessCount = 0
guessLimit = 5
outofGuess = False
while guess != secretWord and not(outofGuess):
    if guessCount < guessLimit:
        guess = input("Enter the Guess: ")
        guessCount += 1
    else:
        outofGuess = True

if outofGuess:
    print("OUT OF GUESS!!! SORRY :(")
else:
    print("Hurray you win!!!")    