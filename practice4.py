import random
print(4**2)
print(16//2)
this_list=[random.randint(100, 200) for x in range(8)]
print(this_list)
this_list2=["1", '2' , '3', '4', '5' ]
print(this_list2)
print(this_list[1])
this_list2.insert( 1, '3')
print(this_list2)
this_list2.remove('3')
print(this_list2)
this_list2[2:5] = [ '11', '12', '13']
print(this_list2)
this_list2[3:10] = [ random.randrange(20, 100) for x in range(11)]
print(this_list2)
this_list2[3:10] = [ random.randrange(20, 100) for x in range(11)]
print(this_list2)
this_list2[5:15] = [ 42 ]
print(this_list2)
this_list2.insert(5, 42)
print(this_list2)
this_list2.append(444)
this_list2.extend(this_list)
print(this_list2)
[print(x) for x in this_list2]