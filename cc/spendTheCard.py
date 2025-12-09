import json
from loadData import loadData

def spendtheCard():
    card_num=input('enter card number:')
    spend_amount=int(input('enter the amount to be spend: '))
    data=loadData()
    found=False
    for card in data:
        if card["ccnum"]==card_num:
            found=True
            if card["limit"]<spend_amount:
                print("cannot process the transaction due to unavailibilty of limit")
            else:
                card["limit"]-=spend_amount
                card["outstanding"]+=spend_amount
                print(f"transation success ! available limit is {card['limit']} and outstanding is {card['outstanding']}")
            break
    if not found:
        print("invalid card num")
    with open("ccdata.json","w")as f:
        json.dump(data,f,indent=4)
