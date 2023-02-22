import random

def is_prime(n):
    if n<= 1:
        return False
    for x in range(2, int(n*0.5)+1):
        if n%x==0:
            return False
    return True
def closest_toAvrg(n):
    return abs(n - 50)

this_list=[ random.randint(1, 100) for x in range(10)]
oddNumList= [ x for x in this_list if x%2==1]
evenNumList = [ x for x in this_list if x%2 == 0]
primeNumList   = [ x for x in this_list if is_prime(x)==True]
print(this_list)
print(oddNumList)
print(evenNumList)
print(primeNumList)

oddNumList.sort()
print(oddNumList)
evenNumList.sort(reverse=True)
print(evenNumList)
this_list.sort(key=closest_toAvrg)
print(this_list)




