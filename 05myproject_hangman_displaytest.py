graveyard = (input("Many letters pls:  "))
graveyard.strip(" ")
nursery = graveyard[:]
print(graveyard, len(graveyard))

#graveyard=[]
#nursery=[]
guessedLetter = "q"

answer = "birthday"

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

if len(graveyard) == 11:
    print(hangman12n)
elif len(nursery) == len(answer):
    print(hangman13n) 
