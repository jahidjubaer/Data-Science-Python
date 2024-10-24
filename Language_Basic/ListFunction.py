mylist = [4,3,4,5,2,8,1,3]
mylist2 = [4,3,2,5,6,2,4,6]

mylist.extend(mylist2) #mylist extended
print(mylist)

#insert value
mylist.insert(3,1)
print(mylist)

#return index for value
print(mylist.index(5))

#remove value
mylist.remove(4)
print(mylist)

#pop the last element
mylist.pop()
print(mylist)
#pop the value by index
mylist.pop(4)
print(mylist)

#sort
mylist.sort()
print(mylist)

#reverse
mylist.reverse()
print(mylist)
