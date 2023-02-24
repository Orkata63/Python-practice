#https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

if __name__ == '__main__':

    height, width = input().split()
    height, width = int(height), int(width)
    pDesign = '.|.'
    fDesign = '---'
    for x in range(height):
        for y in range(width):
            if not int(x) == int(len(range(height))/2) and int(y) == int((width/2+1)):
                if int(x) < int(height/2):
                    factor = int(height/2) - int(x)
                    newLine = fDesign*factor + pDesign * (int(width/3) - int(factor*2)) + fDesign * factor
                if x > int(height/2):
                    factor =  int(x) - int(height/2)
                    newLine = fDesign * factor + pDesign * (int(width / 3) - int(factor * 2)) + fDesign * factor
            if int(x) == int(len(range(height))/2) and int(y) == int((width/2+1)):
                newLine = "-" * int(width / 2 - 3)+'WELCOME'+ "-"*int(width / 2 - 3)
        print(newLine)

