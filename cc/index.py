import json
from addCard import addCard
from showCards import showCards
from spendTheCard import spendtheCard
from payTheBill import paythebill

def main():
    print("click 1 for adding creditcards")
    print("click 2 for showing credit cards")
    print("click 3 for spending")
    print("click 4 for paying the bill ")
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