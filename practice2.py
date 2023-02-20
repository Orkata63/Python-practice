#print functionality

x = "how much wood can the woodchup"
print(x)
y = "chup if the woodchup wood chup"
print(x,y)
print(x+" "+y)

z, v= 5 , 10
print(z,v)
print(z+v)

print(z,x)



#functions
x = "awesome"

def myfunc():
    print("python is",x)

myfunc()

x = "awesome" #global

def myfunc():
    x = "great" #private
    print("python is",x)

myfunc()
print("python is", x)


def myfunc():
    global x
    x = "great"
    print("python is",x)

myfunc()
print("python is", x)

#data types in python

#strings
x = "this is a string"
y = "this is also a string"

#int
x = 5
y,z,t = 6, 7, 8

#float
x = 20.5
y = z = t = 11.1

#complex
x = 1j
y = complex(3,5) #y= 3 + 5j

#list
x=[1,2,3]
y=list((1,2,3))

#tuple
x=(1,2,3)
y=tuple((1,2,3))

#range
range1 = range(5) #ints from 0 to 4
range2 = range(1,5) #ints from 1 to 4
range3 = range(1,5,2)#ints from 1 to 4 with a increment of 2
print(range1.start)
print(range2.stop)
print(range3.step)
for i in range2:
    if i != range2.stop-1:
        print(i, end=", ")
    else:
        print(i)

import random
print(random.randrange(1,11))
