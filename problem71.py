#https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true
import re
import email.utils
regex = r"^[a-z][\w\-.]*@[a-z]+\.[a-z]{1,3}$" #modified this regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b' that is used for standard emails but since we will have certain emails for the challenge the modified regex is better

if __name__ == "__main__":
    for _ in range(int(input())):
        toParse= input()
        name, em = email.utils.parseaddr(toParse)
        if re.match(regex, em):
            print(toParse)
#dont want to make one liner for clarity and not needing to edit the input string to make a different output, making it redundant

