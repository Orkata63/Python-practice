#https://www.hackerrank.com/challenges/html-parser-part-1/problem?isFullScreen=true
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start : '+tag)
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')

    def handle_endtag(self, tag):
        print('End   : '+tag)

    def handle_startendtag(self, tag, attrs):
        print('Empty : '+tag)
        for attr in attrs:
            print(f'-> {attr[0]} > {attr[1]}')

if __name__ == "__main__":
    
    for _ in range(int(input())):
        MyHTMLParser().feed(input())