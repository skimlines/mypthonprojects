itemPrice = (input("How much does the thing cost?  $")) 
cPaidWa = (input("What did the customer hand you?  $")) 
itemPrice = float(itemPrice) * 100
cPaidWa = float(cPaidWa) * 100 
# cPaidWa: Customer paid with a

while itemPrice > cPaidWa:
    if itemPrice != cPaidWa: 
        print ("\nThe customer did not pay enough money..")
    cPaidWa = (input(f"The item costs ${itemPrice/100}\nWhat did the customer hand you?  $"))
    cPaidWa = float(cPaidWa) * 100 

else: 
    change = float(cPaidWa - itemPrice)
    print (f"The customer paid ${cPaidWa/100} and the item's price is ${itemPrice/100}. Change to be paid is ${change/100} in:\n")    

    nPennies = int(change % 5)
    nNickels = int(((change % 10) - (change % 5)) / 5)
    nDimes = int(((change % 25) - (change % 10)) / 10)
    nQuarters = int(((change % 100) - (change % 25)) / 25)
    nSingles = int(((change % 500) - (change % 100)) / 100)
    nFives = int(((change % 1000) - (change % 500)) / 500)
    nTens = int((change - (change % 1000)) / 1000)
    
    # idk why but sometimes there's a nickel missing from the calculations; therefore this patch checks if there is a mismatch between change and number of nickels:
    if ((nTens * 1000) + (nFives * 500) + (nSingles * 100) + (nQuarters * 25) + (nDimes * 10) + (nNickels * 5) + (nPennies * 1))/100 != change:
        print ("Nickel mismatch detected.")
        nNickels += 1
        if nNickels == 2:
            nNickels = 0
            nDimes += 1

    print ("|    Tens   |   Fives   |  Singles  |  Quarters  |   Dimes   |  Nickels  |  Pennies  |")
    print ("+=" * 43)
    print (f"|     {nTens}     |     {nFives}     |     {nSingles}     |      {nQuarters}     |     {nDimes}     |     {nNickels}     |     {nPennies}     |")
    print ("Final count:  $", ((nTens * 1000) + (nFives * 500) + (nSingles * 100) + (nQuarters * 25) + (nDimes * 10) + (nNickels * 5) + (nPennies * 1))/100)
    