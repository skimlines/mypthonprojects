# This program takes a string of letters from the user and sorts them alphabetically. It does this by taking the string, converting it to a list, then sorting it alphabeitcally, and then it converts the list back into a string.
# This program checks for duplicate letters!!!

graveyard = ''
answer = ''

# while loop to keep the programming running until 'quit'
while answer != "quit":

    answer = input("What to add? ")
    print ("Type quit to quit")

    graveyard += answer

    # Checks for duplicates and only adds unique letters
    new_list = []
    for each_letter in graveyard:
        if each_letter not in new_list:
            new_list.append(each_letter)
#    print(new_list)
    graveyard = new_list[:]
    del new_list

    graveyard = sorted(graveyard)

    # list -> string
    graveyard = ''.join(graveyard)

    print("The graveyard contains: ", graveyard)