import json
def loadData():
    with open("ccdata.json","r") as f:
        data=json.load(f)
    return data