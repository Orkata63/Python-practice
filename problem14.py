#https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def average(array):
    # your code goes here
    new_set = set(array)
    average = sum(new_set)/len(new_set)
    return "{0:.3f}".format(average)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
