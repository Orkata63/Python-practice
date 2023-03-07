#https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true
import re
regex = r"^(7|8|9)[0-9]{9}$" #also can be r"^[789]/d{9}$"
if __name__ == "__main__":
    [print("YES" if re.match(regex, input()) else "NO") for _ in range(int(input()))]
