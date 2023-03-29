
def add(x, y):
    return x+y

def subtraction(x, y):
    return x - y

def multiply(x, y):
    return x*y

def divide(x, y):
    if y == 0:
        raise ValueError("Can no divide by zero!")
    return int(x/y)



