#https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true
import re

if __name__ == "__main__":
    T = int(input())
    for x in range(T):
        try:
            re.compile(input())
            print(True)
        except re.error:
            print(False)