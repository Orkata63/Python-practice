#https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true
import re

if __name__ == "__main__":
    regex = r"^[+-]?[0-9]*[.][0-9]+$" # ^ meta starts, $ meta ends [] -> any element in them ? 1 time; * one or more times ; + one "." and more 2nd [] elements
    [print(True if re.match(regex, input()) else False) for _ in range(int(input()))]


