#https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true


if __name__ == "__main__":
    numA = int(input())
    A = set(map(int, input().split()))
    for n in range(int(input())):
        comL = str(input())
        newS = set(map(int, input().split()))
        if comL[:6] == "update":
            A.update(newS)
        if comL[:19] == "intersection_update":
            A.intersection_update(newS)
        if comL[:27] == "symmetric_difference_update":
            A.symmetric_difference_update(newS)
        if comL[:17] == "difference_update":
            A.difference_update(newS)
    print(sum(A))

    # works for the test but number on set size is not used, and dont know how to use a smarter way of calling the functions