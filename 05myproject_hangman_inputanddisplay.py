print ("\n\t\t\tLet's play hangman!!!")
answer = "birthday"

def wordDisplay():
    for characters in answer:
        n = 0
        for letters in nursery:
            print (letters, end=" ")
            n += 1 
        else:
            print ("_", end=" ")
            n += 1
    print ("\n")

graveyard = []
nursery = []

# Game over conditions:
# 1. if the user guesses the word
# 2. if the user runs out of guesses (11 guesses)

def mainGame():

    if len(nursery) != len(answer):

        if userGuess in answer:
            print (f"Yes! {userGuess} is in the word.")
            nursery.append(userGuess)    

        elif userGuess not in answer:
            print (f"Nope, {userGuess} ain't in there.")
            graveyard.append(userGuess)

        else:
            print ("Huh?")
        nursery.sort()
        graveyard.sort()

    else: 
        if len(nursery) == len(answer):
            print ("You win!", end=" ")

        if len(graveyard) == len(answer):
            print ("You lose!", end=" ")


userGuess = ""
while userGuess != 'quit':
    
    wordDisplay()
    userGuess = input("What letter do you guess?  ")
    print("Type quit to exit")
    print(f"\tCorrect guesses: {nursery.sort()} \t  Wrong Guesses: {graveyard.sort()}" )

    if userGuess != 'quit':
        mainGame()
    
print ("The answer was", answer)
