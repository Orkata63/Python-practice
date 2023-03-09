#https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
import collections
from collections import OrderedDict


if __name__ == "__main__":
    words = list()
    for _ in range(int(input())):
        words.append(input())
    words1 = collections.Counter(words)
    print(len(words1))
    print(" ".join(str(x) for x in words1.values()))