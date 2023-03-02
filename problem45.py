#https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true&h_r=next-challenge&h_v=zen


if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    for _ in range(int(input())):
        newL = str(input())
        if  newL == "pop":
            s.pop()
        if newL[:6] == "remove":
            s.remove(int(newL[7:]))
        if newL[:7] == "discard":
            s.discard(int(newL[8:]))
    print(sum(s))

