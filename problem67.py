#https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true
import re
#AEIOU
#aeiou
#QWRTYPSDFGHJKLZXCVBNM
#qwrtypsdfghjklzxcvbnm
#given in the challenge


if __name__ == "__main__":
    match = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])[AEIOUaeiou]{2,}(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])', input())
    print(*match if len(match) > 0 else [-1], sep='\n')



#    match = re.findall(r'[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM][AEIOUaeiou]{2,}[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]', input())
#  this is finding the correct target just need to isolate vowels
# (?<=x)y will return y if there is xy in order
# y(?=x) will return x if xy in order found these formats