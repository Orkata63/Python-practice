#https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true

cube = lambda x: x**3 # complete the lambda function

def fibonacci(n):
    # return a list of fibonacci numbers
    fib = []
    for x in range( n):
        if x == 0:
            fib.append(0)
        if x == 1:
            fib.append(1)
        if x >= 2:
            fib.append(fib[x-2]+fib[x-1])
    return fib
#originally made fib = [ 0 , 1] but test on hacker rank had cases with 0 and 1 so had to make if statements
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))