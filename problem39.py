#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true
#challenge to have a solution in 4 or less than 4 lines of code
from collections import namedtuple

if __name__ == "__main__":
    N = int(input())
    students = namedtuple("Students",input().split())
    print(format((sum(int(students(*input().split()).MARKS) for x in range(N)) / N), '.2f'))
