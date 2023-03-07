#https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

def merge_the_tools(string, k):
    # your code goes here
    uniqL = set()
    for x in range(int(len(string) / k)):
        printStr = ""
        for y in string[x * k:(x + 1) * k]:
            if y not in uniqL:
                uniqL.add(y)
                printStr += printStr.join(y)
        print(printStr)
        uniqL.clear()
    return 0
    # not satisfied with the solution

    #print(*["".join(set(string[y*k:(y+1)*k])) for y in range(int(len(string)/k))], sep='\n') doesnt work since print out is off
    #reason why im forced to use set() to make sure the print is correct



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

