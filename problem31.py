#https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true

from collections import defaultdict


if __name__ == "__main__":

    d = defaultdict(list)
    d1 = defaultdict(list)

    n , m = map(int, input().split(" "))

    for n in range(1, n+1): #the challence requires using 1 as start
        d[n] = input()

    for m in range(1, m+1):
        d1[m] = input()

    for key1, value1 in d1.items():
        result = ""
        check = False
        for key, value in d.items():
            if value == value1 :
                result = result+str(key) + " "
                check = True
        print(result if check==True else "-1")

