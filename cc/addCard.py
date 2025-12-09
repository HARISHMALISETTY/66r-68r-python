import json
from loadData import loadData
def addCard():
    username=input("enter username: ")
    password=input("enter password: ")
    ccnum=input("enter credit carf number: ")
    limit=int(input("enter cc limit: "))
    outstanding=0
    cc_card={'username':username,'password':password,'ccnum':ccnum,'limit':limit,'outstanding':outstanding}
    data=loadData()
    data.append(cc_card)
    with open('ccdata.json','w')as f:
        json.dump(data,f,indent=4)
    print("creditcard addedd successfully")