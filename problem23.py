#https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def count_substring(string, sub_string):
    counter = 0
    for x in range(0,len(string)-len(sub_string)+1):
        if string[x:x+len(sub_string)] == sub_string:
            counter+=1
    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)