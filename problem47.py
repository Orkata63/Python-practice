#https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true

from collections import deque

if __name__ == "__main__":
    N = int(input())
    d = deque()
    for _ in range(N):
        newl = str(input())
        if newl[:6] == "append" and newl[6] == " ":
            d.append(int(newl[7:]))
        if newl[:10] == "appendleft":
            d.appendleft(int(newl[11:]))
        if newl == "pop":
            d.pop()
        if newl == "popleft":
            d.popleft()
    print(" ".join(str(d[x]) for x in range(len(d))))
#worked in pypy 3 but not python 3 on HackerRank website