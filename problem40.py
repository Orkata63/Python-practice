#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
from collections import OrderedDict

if __name__ == "__main__":
    N = int(input())
    orderedDict = OrderedDict()
    for x in range(N):
        item_name = ''
        net_price = ''
        inStr = input()
        for x in range(len(inStr)):
            if x in range(len(inStr)-1) and not inStr[x+1].isdigit():
                item_name += inStr[x]
            if inStr[x].isdigit():
                net_price += inStr[x]
        orderedDict[item_name] = orderedDict.get(item_name, 0) + int(net_price)

    [print(x, y) for x,y  in orderedDict.items()]

