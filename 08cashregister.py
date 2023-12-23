itemPrice = (input("How much does the thing cost?  $")) 
cPaidWa = (input("What did the customer hand you?  $")) 
itemPrice = float(itemPrice) * 100
cPaidWa = float(cPaidWa) * 100 
# cPaidWa: Customer paid with a

while itemPrice > cPaidWa:
    if itemPrice != cPaidWa: 
        print ("\nThe customer did not pay enough money..")
    cPaidWa = (input(f"The item is {itemPrice}. \nWhat did the customer hand you?  $"))
    cPaidWa = float(cPaidWa) * 100 

else: 
    change = cPaidWa - itemPrice

    print (f"The customer paid ${cPaidWa/100} and the item's price is ${itemPrice/100}. Change to be paid is ${change/100} in:")    
    nSingles = int(change / 100)
    nQuarters = int(change-(nSingles*100)) / 25
    nDimes = int(change-(nSingles*100)-(nQuarters*25)) / 10
    nNickels = int(change-(nSingles*100)-(nQuarters*25)-(10*nDimes)) / 5
    nPennies = int(change-(nSingles*100)-(nQuarters*25)-(10*nDimes)) % 5
    print (f"Change to be given: \n\tSingles: {nSingles}\n\tQuarters: {nQuarters}\n\tDimes: {nDimes}\n\tNickels: {nNickels}\n\tPennies: {nPennies}")