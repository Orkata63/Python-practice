#https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true
#unelegant solution
import cmath
import math

if __name__ == "__main__":
    strInput = input()
    listInput = strInput[:-1].removeprefix("-")
    if "+" in listInput:
        listInput = listInput.split("+")
    if "-" in listInput:
        listInput = listInput.split("-")
    if "-" in strInput and strInput[0]=='-':
        real = strInput[:len(listInput[0])+1]
    else:
        real = strInput[:len(listInput[0])]
    if "-" in strInput and (strInput[1] == "-" or strInput[2]=="-"):
        imagine = strInput[len(real):-1]
    else:
        imagine = strInput[len(real)+1:-1]

    print(math.sqrt(int(real)**2 + int(imagine)**2))
    print(cmath.phase(complex(int(real),int(imagine))))