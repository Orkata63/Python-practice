#https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true
import re

if __name__ == "__main__":
    S = input()
    k = input()
    matches = list(re.finditer(rf'(?={k})', S))
    if matches:
        for m in matches:
            print((m.start(), m.start() + len(k) - 1))
    else:
        print((-1, -1))
