def addCard():
    print("adding function is executing")
def showCards():
    print("showcards function is executing")
def spendtheCard():
    print("spend card funciton is executing")
def paythebill():
    print("pay bill funciton is executing")
def main():
    print(" click 1 for adding creditcards , click 2 for showing credit cards,click 3 for spending,click 4 for paying the bill ")
    ip=int(input("enter ur choice: "))
    if ip==1:
        addCard()
    elif ip==2:
        showCards()
    elif ip==3:
        spendtheCard()
    elif ip==4:
        paythebill()
    else:
        print("enter correct choice")
main()