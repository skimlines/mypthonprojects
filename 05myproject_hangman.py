losingScore = 10
userScore = gameScore = 0

# When the player has this many tries left, a hint is displayed
difficultyLevel = 2

# Create a wordBank based on the capitals in each state.
capital_state = {
    'Montgomery':'Alabama',
    'Juneau':'Alaska',
    'Phoenix':'Arizona',
    'Little Rock':'Arkansas',
    'Sacramento':'California',
    'Denver':'Colorado',
    'Hartford':'Connecticut',
    'Dover':'Delaware',
    'Tallahassee':'Florida',
    'Atlanta':'Georgia',
    'Honolulu':'Hawaii',
    'Boise':'Idaho',
    'Springfield':'Illinois',
    'Indianapolis':'Indiana',
    'Des Moines':'Iowa',
    'Topeka':'Kansas',
    'Frankfort':'Kentucky',
    'Baton Rouge':'Louisiana',
    'Augusta':'Maine',
    'Annapolis':'Maryland',
    'Boston':'Massachusetts',
    'Lansing':'Michigan',
    'Saint Paul':'Minnesota',
    'Jackson':'Mississippi',
    'Jefferson City':'Missouri',
    'Helena':'Montana',
    'Lincoln':'Nebraska',
    'Carson City':'Nevada',
    'Concord':'New Hampshire',
    'Trenton':'New Jersey',
    'Santa Fe':'New Mexico',
    'Albany':'New York',
    'Raleigh':'North Carolina',
    'Bismarck':'North Dakota',
    'Columbus':'Ohio',
    'Oklahoma City':'Oklahoma',
    'Salem':'Oregon',
    'Harrisburg':'Pennsylvania',
    'Providence':'Rhode Island',
    'Columbia':'South Carolina',
    'Pierre':'South Dakota',
    'Nashville':'Tennessee',
    'Austin':'Texas',
    'Salt Lake City':'Utah',
    'Montpelier':'Vermont',
    'Richmond':'Virginia',
    'Olympia':'Washington',
    'Charleston':'West Virginia',
    'Madison':'Wisconsin',
    'Cheyenne':'Wyoming',
    }
wordBank = []
for capitals in capital_state.keys():
    wordBank.append(capitals)

# Choose a random state capital as the answer
import random
answer = wordBank[random.randrange (0,len(wordBank))]
answerKeys = answer.upper()

def main_game(gameScore, userScore):
    # Graveyard stores wrong answers as a string
    # nursery stores right answers as a string
    # User Guess is the user's guess as a string
    # Game message displays messages next to the hangman as a string 
    graveyard = nursery = userGuess = gameMessage = ''

    # Choose a random city as the answer
    import random
    answer = wordBank[random.randrange (0,len(wordBank))]
    answerKeys = answer.upper()

    # Creates an answerKeys from the answer & omits any spaces in a name 
    newList = []
    for eachLetter in answerKeys:
        if eachLetter != ' ':
            if eachLetter not in newList:
                newList.append(eachLetter)
    newList = ''.join(sorted(newList))
    answerKeys = newList[:]
    del newList

    # The high quality cutting edge AAA graphics:
    hangman1n = '\t  +-----+       '
    hangman2 = '\t  |     |       '
    hangman3 = '\t  |    WWW      '
    hangman5 = "\t  |   q'A'p     "
    hangman6 = '\t  |    /Y\      '
    hangman7 = '\t  |   / | \     '
    hangman9 = "\t  |  ' / \ '    "
    hangman10 = '\t  |    \ /      '
    hangman12 = '\t  |    j L      '
    hangman10n = '\t  |             '

    #only the left ear
    hangman4 = "\t  |   q'A      "

    #just the left foot
    hangman11 = '\t  |    j        '

    #right hand and thighs
    hangman8 = "\t  |      \ '    "

    #face when dead
    hangman13 = '\t  |   qX_Xp     '
    hangman14 = "\t  |   q'u'p     "
    hangman12n = '\tY O U  L O S T !'
    hangman13n = '\tY O U  W  O  N !'

    #empty hang
    hangman2n = hangman10n
    hangman3n = hangman10n
    hangman4n = '\t  |  H E L P    '
    hangman5n = hangman10n
    hangman6n = '\t  |    M E      '
    hangman7n = hangman10n
    hangman8n = '\t  |     !       '
    hangman9n = hangman10n

    # hangman apperance logic
    def graphics(answerKeys, graveyard, nursery):
        # The bank is mainly for checking if the game started yet
        bank = graveyard + nursery

        print(hangman1n) # The top

        # The noose  
        if len(graveyard) > 0:
            print (hangman2)
        elif nursery == answerKeys:
            print(hangman2n)
        elif len(bank) == 0:
            print (hangman2n)

        # The hair
        if len(graveyard) > 1:
            print(hangman3, end='\t')
        else:
            print(hangman3n, end='\t')

        print('Wrong guesses: ', end='')
        for eachLetter in graveyard.upper():
            print(eachLetter, '', end='')
        print()

        # The head
        if nursery == answerKeys:
            print (hangman14)
        elif len(graveyard) >= losingScore:
            print (hangman13)
        elif len(graveyard) == 3: # left face
            print (hangman4)
        elif len(graveyard) > 3:
            print (hangman5)
        elif len(bank) == 0:
            print (hangman4n)
        else:
            print (hangman2n)

        # The shoulders
        if len(graveyard) > 4:
            print(hangman6, end='\t')
        else:
            print(hangman5n, end='\t')

        print('Correct guesses: ', end='')
        for eachLetter in nursery.upper():
            print(eachLetter, '', end='')
        print()

        # Lower arms
        if len(graveyard) > 5:
            print (hangman7)
        elif len(bank) == 0:
            print (hangman6n)
        else:
            print (hangman2n)

        # Hands1
        if len(graveyard) == 7: # Right hand
            print (hangman8, end='')
        elif len(graveyard) > 7:
            print (hangman9, end='')
        else:
            print (hangman7n, end='')

        print(gameMessage)

        #lower legs
        if len(graveyard) == losingScore:
            print(hangman12n)
        elif nursery == answerKeys:
            print(hangman13n)
        elif len(graveyard) > 8:
            print(hangman10)
        elif len(bank) == 0:
            print(hangman8n)
        else:
            print(hangman2n)

        #feet and platform
        if len(graveyard) == 10: # Left foot
            print(hangman11, end='')
        elif len(graveyard) > 10:
            print(hangman12, end='')
        else:
            print(hangman9n, end='')
        print(end='\t')

    def word_display(answerKeys):
        # Word Display
        for characters in answer.upper():
            if characters == ' ':
                print(' ', end=' ')
                answerKeys = answerKeys.strip()
            elif characters in nursery:
                print(characters, end=' ')
            else:
                print('_', end=' ')
        
        
        gameScore = losingScore - len(graveyard)
        if gameScore <= difficultyLevel:
            print(f' (Hint: {capital_state[answer]})', end='')
        
        print('\n\t  |             ')
        print('\tTTTTTTTTTTTTTTT         ', end='')
        
        print(f'Guesses left: {gameScore}')
        if nursery != answerKeys and len(graveyard) != losingScore:
            print("\n\tGuess the state capital I'm thinking of, and the hangman will be spared!    \n\t(Hit enter with no input to quit)")
        
    def quitting(userGuess):
        quitting = input('Did you want to quit playing? Y/N ')
        if quitting.upper() == 'Y':
            print(' ~' * 42)
            print('\n\t~*~*~*~ Thanks for playing. Good bye! ~*~*~*~\n')
            print(' ~' * 42)
            exit()
        else:
            graphics(answerKeys, graveyard, nursery)
            word_display(answerKeys)
            print ("Oh, ok! Let's continue then.")    
            userGuess = input('\n What letter do you guess? ')
            return userGuess
        
    while nursery != answerKeys:
        graphics(answerKeys, graveyard, nursery)
        word_display(answerKeys)
        userGuess = input('\n What letter do you guess? ')

        # If the user quits
        while userGuess == '':
            quitting(userGuess)

        userGuess = userGuess.upper()

        if userGuess in answerKeys:
            gameMessage = f'\tYeah, {userGuess} is in the word'
        elif userGuess not in answerKeys:
            gameMessage = f'\tOh no, {userGuess} is not in the word........'

        # If you put in a letter you already used
        bank = nursery + graveyard
        while userGuess in bank:
            gameMessage = f"\tYou've already guessed a {userGuess}..."
            graphics(answerKeys, graveyard, nursery)
            word_display(answerKeys) 
            userGuess = input('\tGuess a different letter!  ')
            # If the user quits
            while userGuess == '':
                quitting(userGuess)
            userGuess = userGuess.upper()
        del bank

        # Game scoring 
        if userGuess in answerKeys:
            nursery = nursery + userGuess
            nursery = ''.join(sorted(nursery))
        else:
            graveyard = graveyard + userGuess
            graveyard = ''.join(sorted(graveyard))

        # If you lose
        gameScore = losingScore - len(graveyard)
        if gameScore <= 0:
            graphics(answerKeys, graveyard, nursery)
            word_display(answerKeys)
            print()
            print('- ' * 42)
            print(f'\nYou Lose....The answer was {answer}\n')
            print('- ' * 42)
            break
    else:
        graphics(answerKeys, graveyard, nursery)
        word_display(answerKeys)
        print()
        print('*~' * 42)
        print(f'\nYou win!!!!! The answer was {answer}, the state capital of {capital_state[answer]}\n')
        userScore += 1
        print(userScore)
        print('*~' * 42)
    return userScore
    
gameContinue = 'y'
nRounds = 0
while gameContinue == 'y':
    nRounds += 1
    userScore = main_game(gameScore, userScore)
    print (f'Number of rounds won: {userScore} out of {nRounds} rounds. ')
    gameContinue = input('Play again? \nY to play again, any other key to quit!  ')
    gameContinue = gameContinue.lower()

print('*~' * 42)
print("Thanks for playing. Bye!")
print("skimlines@noc.social on mastodon")
print('*~' * 42)
