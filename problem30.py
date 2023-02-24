#https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
import string

def print_rangoli(size):
# your code goes here
# this is meant to be a single string solution
    rangoli = ""
    alhpa = list(string.ascii_lowercase)
    aLocation = ( size -1, size -1)
    for x in range(size*2-1):
        for y in range(size*2-1):
            if distance_from_center(x , y, aLocation) <= int(size-1) and x != size*2-1:
                rangoli = rangoli+alhpa[distance_from_center(x,y,aLocation)]+"-"
            elif x == aLocation[0] and y == aLocation[1]:
                rangoli = rangoli + "-a"
            else:
                rangoli = rangoli + "--"
        if int(x) != range(size*2-1)[-1]:
            rangoli = rangoli.removesuffix("-") + "\n"
    print(rangoli.removesuffix("-"))

def distance_from_center(x,y, center):
    return (abs(center[0] - x  ) + abs( center[1] - y))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)