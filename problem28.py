#https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true

def print_formatted(number):
    # your code goes here
    maxWidth = len(bin(range(number+1)[-1])) - 2 #the -2 isnt needed its there to offset the test different caused do to some extra offset that couldnt be fixed otherwise
    for x in range(1, number+1):
        print("{:>{w}} {:>{w}} {:>{w}} {:>{w}}".format(str(x), str(oct(x)[2:]), make_upper(str(hex(x)[2:])),str(bin(x)[2:]), w = maxWidth))
def make_upper(hexNum):
    if hexNum.islower():
        return hexNum.upper()
    else:
        return hexNum
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)