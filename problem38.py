#https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true

if __name__ == "__main__":
    T = int(input())
    for x in range(T):
        a,b = map(str, (input()).split(" "))
        try:
            print(int(a) // int(b))
        except ZeroDivisionError as e:
            print( "Error Code:",e )
        except ValueError as e:
            print("Error Code:", e )
