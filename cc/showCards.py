import json
from loadData import loadData

def showCards():    
    data=loadData()
    if len(data)==0:
        print("no cards available")
    else:
        for card in data:
            print(card)
    print("showcards function is executing")
