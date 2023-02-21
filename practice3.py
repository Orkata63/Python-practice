#Strings
a = ' String '
print(a)
b = "also a string"
print(b)
c = '''A string that can take 
multiple lines 
and be printed as such'''
#should be at the strat to mimic that of the classic word alignment
print(c)
print(a[3])
print(len(c))
for x in a:
    print(x)

print("string" in c) #returns bolean
print('bomb' not in c)
if ("Hello,World" not in c):
    print("yes this isnt the default code")

'''  
n=str(input())
print(n)
'''

#slicing
print(b[1:4])
print(b[:4])
print(b[2:])
print(b[-6:-1])

print(a.upper())
print(a.upper().lower())
print(a.strip())
print(c.split())
print(a.replace("S","R"))

#formating
age = 24
txt = "My name is John and im {}"
print(txt.format(age))

#also works with multiples
height = 100
weight = 10
extendedText = txt + " im also {} tall and i weigh {}"
print(extendedText.format(age,height,weight))
#these {} can also be indexed to make precise formating

example = "we are the so called \"Vikings\" from somewhere"
print(example)
print(example.capitalize())
print(example.casefold())
print(example.encode())
print(example.swapcase())


