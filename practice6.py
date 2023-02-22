
thisset = { "apple", "banana" , "cherry" }
print(thisset)
thisset1 = { "apple", "banana" , "cherry", "apple" }
print(thisset1)
thisset2 = { "apple", "banana" , "cherry", 1 , True }
print(thisset2)
for x in thisset:
    print(x)


this_list = ("hello", "world")
print("orange" in thisset)

thisset.add("orange")
print(thisset)
thisset.update(thisset2)
print(thisset)
thisset.update(this_list)
print(thisset)
thisset3 = thisset.union(thisset2)
thisset4 = thisset.intersection(thisset3)
print(thisset4)
print(thisset3)


thisdict = {
    "Student": "Rick",
    "year": "Third",
    "GPA": 3.6
}
print(thisdict)
newDict= dict(Student="Kennedy", year = "Second", GPA=3.2 )
print(newDict)

