#https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true
regex = r"#[0-9A-Fa-f]{6}|#[0-9A-Fa-f]{3}" # order of 6 then 3 matters
import re

if __name__ == "__main__":
    colors = list()
    for _ in range(int(input())):
        S = input()
        if S.endswith(";"): # so it`s not a separator
            colors+=re.findall(regex, S)
    print(*colors, sep= "\n")