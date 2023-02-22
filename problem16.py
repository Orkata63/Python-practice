#https://www.hackerrank.com/challenges/no-idea/problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&isFullScreen=true
if __name__ == '__main__':
    Happiness = 0
    firstInput = list(map(int, input().split(" ")))
    n = firstInput[0]
    m = firstInput[1]
    secondInput = list(map(int, input().split(" ")))
    thirdInput = list(map(int, input().split(" ")))
    fourthInput = list(map(int, input().split(" ")))
    finalA = set(thirdInput).difference(set(fourthInput))
    finalB = set(fourthInput).difference(set(thirdInput))
    for x in secondInput:
        if x in finalA:
            Happiness+=1
        elif x in finalB:
            Happiness-=1
    print(Happiness)

