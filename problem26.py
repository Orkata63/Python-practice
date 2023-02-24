#https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import textwrap #give from hackerrank

"""
def wrap(string, max_width):
    return textwrap.wrap(string, max_width) #read how it works

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    [print(r) for r in result]
""" # doesnt work the way its intended

def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
#the way its intended to work
