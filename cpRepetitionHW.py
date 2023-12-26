#*******************************************************************************
#
# Programmer: MISSION RAJ KADARIYA
#
# Assignment: cpRepetitionHW.py
#
# Description: This program is about dice roll game. It start with a credit
#              of hundred and ends when a players credit is equal to zero 
#              or you donot have enough credit to bet. A player wins when 
#              the guess is correct and he loose when its incorrect or equal
#              to computer roll.
#               
#           
#
#*******************************************************************************

#imports random
import random
#prompting the user to place a bet or quit
credit = 100
startRound = int(input("Enter 1 to Place a bet. Enter 2 to Quit the game:"))
if startRound == 1:
    while credit > 0: # game will continue unless credit is equal to zero
        #prompting user to place a bet
        a = int(input("How much you want to bet (1-25):"))
        #creating the condition to run the game
        if 1 <= a <= 25 and a <= credit:
           #calculations
            credit = credit - a
            #generate the random number between
            computerRoll = random.randint(1, 6) + random.randint(1,6)
            playersRoll = random.randint(1, 6) + random.randint(1,6)
           #prompting user to guess over or under
            guess = input("If your roll is Over or Under?")
            if (guess.lower() == "over" and playersRoll > computerRoll) or \
                (guess.lower() == "under" and playersRoll < computerRoll):
                # displaying the result if the guess is correct
                print("You win :)")
                print("Computer roll = ", computerRoll)
                print("Your roll = ", playersRoll)
                a = a * 1.5 #calculations
                nextRound = input("Play double or nothing (y/n)") # Using boolean expression
                if nextRound == "y":
                    # generates the random number between
                    computerRoll = random.randint(1, 6) + random.randint(1, 6)
                    playersRoll = random.randint(1, 6) + random.randint(1, 6)
                    #prompting user to guess over or under
                    guess = input("If your roll is Over or Under?")
                    #if and or statement 
                    if (guess.lower() == "over" and playersRoll > computerRoll) or \
                        (guess.lower() == "under'\n"
                     and playersRoll < computerRoll):
                        #displaying the result if the if and or statement is true
                        print("You win :)")
                        print("Computer roll = ", computerRoll)
                        print("Your roll = ", playersRoll)
                        #calculations
                        a = 2 * a
                        credit = credit + a
                        print("Your credit is", credit)
                    # displaying the result if the player lose
                    else:
                        print("You lose")
                        print("Computer roll = ", computerRoll)
                        print("Your roll = ", playersRoll)
                        #calculations
                        a = a / 1.5
                        credit = credit + a
                        #printing the credit after match ends
                        print("Your credit is", credit)
                    #promting user if they want to continue the game
                    playAgain = input("Do you wanna play again (y/n):")
                    #displayig if the player doesnot want to continue
                    if playAgain == "n":
                        print("Game Ended!!!")
                        print("Your current credit is", credit)
                        quit()
                #displaying if player win and doesnot want to continue
                else:
                    print("You win:)")
                    #calculations
                    a = 1.5 * a
                    credit = credit + a
                    print("Your New Credit is", credit)
            #displaying the results if the player lose
            else:
                print("YOU LOOSE :(")
                print("Your current credit is", credit)
                 #promting user if they want to continue the game
                playAgain=input("Do you wanna play again (y/n):")
                #displaying if the player doesnot want to continue
                if playAgain == "n":
                    print("Game Ended!!!")
                    print("Your current credit is", credit)
                    quit()
        #displaying the results if the player doesnot have enough credit
        else:
            print("Bet Amount Invalid!!!")
#ending the code with else statement
else:
    print("LOSER!!!!")
    quit()