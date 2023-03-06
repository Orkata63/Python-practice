"""import math
x = ( 5 , 10 , 1, 23, 21, 23, 5135, 121, 1321)
print(max(x), min(x))
print(math.pi)"""
"""
import json

x =  {
    "name":"John",
    "age":30,
    "city":"New York"
}

y = json.dumps(x)

print(y)
"""
"""
import re
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
"""
"""
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt)) 
"""
"""
username = input("Enter username:")
print("Username is: " + username)
"""
import os
#text = open("text.txt", "r")
#print(text.read())
#print(text.read(10))
#print(text.readline())
#print(["".join(text.read(20)) for x in range(5)])
#text.close()
if os.path.exists("text.txt"):
    os.remove("text.txt")
else:
    print("The file doesnt exist")