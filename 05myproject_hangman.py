answer = "Birthday"

for char in answer:
    print ("_", end=" ")

graveyard=[]
nursery=[]
guessedLetter = "q"
turnIndex = 0

hangman1n = "     +-----+       "
hangman2 = "     |     |       "
hangman3 = "     |    WWW      "
hangman5 = "     |   q'A'p     "
hangman6 = "     |    /Y\      "
hangman7 = "     |   / | \     "
hangman9 = "     |  ' / \ '    "
hangman10 = "     |    \ /      "
hangman12 = "     |    j L      "
hangman10n = "     |             "
hangman11n = "   TTTTTTTTTTTTTTT "

hangman12n = "   Y O U  L O S T !"
hangman13n = "   Y O U  W  O  N !"

#only the left ear
hangman4 = "     |   q'A      "

#just the left foot
hangman11 = "     |    j        "

#right hand and thighs
hangman8 = "     |      \ '    "

#face when dead
hangman13 = "     |   q*0*p     "
hangman13 = "     |   q'u'p     "

#empty hang
hangman2n = "     |             "
hangman3n = hangman2n
hangman4n = "     |  H E L P    "
hangman5n = hangman2n
hangman6n = "     |    M E      "
hangman7n = hangman2n
hangman8n = "     |     !       "
hangman9n = hangman2n

graveyard == (input("Many letters pls:  "))
nursery = graveyard
# hangman apperance logic
print (hangman1n) # The top

# The noose  
if len(graveyard) >= 1:
    print (hangman2)
else: 
    print (hangman2n)

# The hair
if len(graveyard) >= 2:
    print (hangman3)
else:
    print (hangman3n)

# The head
if len(graveyard) >= 3: # left face
    print (hangman4)
elif len(graveyard) >= 4:
    print (hangman5)
elif len(graveyard) >= 11: # Game Over face
    print (hangman13)
elif len(graveyard) > 0 or len(nursery) > 0:
    print (hangman2n)
else:
    print (hangman4n)

# The shoulders
if len(graveyard) >= 5:
    print (hangman6)
else:
    print (hangman5n)

# Lower arms
if len(graveyard) >= 6:
    print (hangman7)
elif len(graveyard) > 0 or len(nursery) > 0:
    print (hangman2n)
else:
    print (hangman6n)

# Hands
if len(graveyard) == 7: # Right hand
    print (hangman8)
elif len(graveyard) >= 8:
    print (hangman9)
else:
    print (hangman7n)

#lower legs
if len(graveyard) >= 9:
    print (hangman10)
elif len(graveyard) > 0 or len(nursery) > 0:
    print (hangman2n)
else:
    print (hangman8n)

#feet
if len(graveyard) >= 10: # Left foot
    print (hangman11)
elif len(graveyard) >= 11:
    print (hangman12)
else:
    print (hangman9n)

print (hangman10n) # The stage
print (hangman11n)

if len(graveyard) == 11: # Left foot
    print (hangman11)


"""
def goGuess():
    guessedLetter = (input("\nGive me a letter "))
    return guessedLetter

#check if the letter was already used or not
if guessedLetter in nursery or graveyard:
    print ("Erm you already guessed that letter...")
    goGuess()

if guessedLetter in answer:
    #if the user enters a letter in the answer, 
    # the program will print a msg abt the correct answer, and then 
    # keep track of the letter by adding it the letter to the nursery. Then I guess 
    # there should be a nursery that states what letters are left to guess. 
    print (f"Yes! {guessedLetter} is one of the letters.")
    nursery.append[guessedLetter]

    turnIndex += 1

else:
    # if the user enters an incorrect letter
    # the program will tell the user that their guess is wrong, 
    # and the incorrect guess is added to the graveyard. 
    # The hangman grows a body part.
    print (f"Nope! {guessedLetter} ain't in there.")
    graveyard.append(guessedLetter)
    
    turnIndex += 1
    
"""