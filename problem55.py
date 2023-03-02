#https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true
from collections import OrderedDict

if __name__ == "__main__":
    """
    N = int(input())
    rooms = OrderedDict()
    s = list(map(int, input().split()))
    for x in s:
        rooms[x] = rooms.get(x, 0) + 1
    print([x for (x, y)  in rooms.items() if y == 1][0])
     """
    #solution with OrderedDict not sure if it was meant to be solved like this
    N = int(input())
    numbers = input()
    print(int((N*sum(set(map(int, numbers.split())))-sum(list(map(int, numbers.split())))) / (N-1)))
    #solution using math