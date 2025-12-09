import json
from loadData import loadData

def paythebill():
    card_num=input('enter card number:')
    pay_amount=int(input('enter the amount to be pay: '))
    data=loadData()
    found=False
    for card in data:
        if card["ccnum"]==card_num:
            found=True
            if card["outstanding"]<pay_amount:
                print("payable amount should not more than outstanding")
            else:
                card["limit"]+=pay_amount
                card["outstanding"]-=pay_amount
                print(f"transation success ! available limit is {card['limit']} and outstanding is {card['outstanding']}")
            break
    if not found:
        print("invalid card num")
    with open("ccdata.json","w")as f:
        json.dump(data,f,indent=4)

