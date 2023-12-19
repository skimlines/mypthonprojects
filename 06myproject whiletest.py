# This program takes a string of letters from the user and sorts them alphabetically. It does this by taking the string, converting it to a list, then sorting it alphabeitcally, and then it converts the list back into a string.

graveyard = ''
answer = ''

while answer != "quit":
    answer = input("What to add? ")
    print ("Type quit to quit")

    graveyard += answer
    graveyard = sorted(graveyard)
    graveyard = ''.join(graveyard)

    print("The graveyard contains: ", graveyard)