#https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true
import re

if __name__ == "__main__":
    regex = r'([0-9a-zA-Z])\1'
    m = re.search(regex, input())
    print(-1 if m == None else m.group(1))

    #test case 1 12345678910111213141516171820212223
    #test case 2 __commit__