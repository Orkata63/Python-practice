#debug problem from https://www.hackerrank.com/challenges/default-arguments/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return
#can only change def print_from_stream()
def print_from_stream(n, stream = EvenStream()):
    for _ in range(n):
        print(stream.get_next())
    stream.__init__() #from testing noticed that it didnt change its current value after endind so just refreshed it manually


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n) # (n, EvenStream()) easy fix  but not allowed on challenge
    else:
        print_from_stream(n, OddStream())
