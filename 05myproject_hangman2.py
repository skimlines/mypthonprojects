answer = "birthday"
for characters in answer:
    print ("_", end=" ")
    print ("\n")

graveyard = []
nursery = []
bank = graveyard + nursery

userGuess = input("What's your guess? ")

if len(nursery) != len(answer):

    if userGuess in answer:
        print (f"Yes! {userGuess} is in the word.")
        nursery.append(userGuess)    

    elif userGuess not in answer:
        print (f"Nope, {userGuess} ain't in there.")
        graveyard.append(userGuess)

    else:
        print ("Huh?")
    print (f"Correct guesses: {nursery.sort()}\nWrong Guesses: {graveyard.sort()}" )

else: 
    if len(nursery) == len(answer):
        print ("You win!", end=" ")

    if len(graveyard) == len(answer):
        print ("You lose!", end=" ")

print ("The answer was", answer)