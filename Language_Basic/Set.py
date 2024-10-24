#set contains unique and sorted value
s = set()
s = {3,4,5,2,4}
print(s)

#it's add 10 , 7
s.add(10)
s.add(7)
# but not add 4 because already in set
s.add(4)
print(s)

s1 = {2, 3, 4, 5, 6}
s2 = {5, 6, 7, 8, 9}
print(type(s1), type(s2))

#all the value in s1 and s2 ; its like union (U)
print(s1 | s2)

#common value in s1 and s2; its like intersection (n)
print(s1 & s2)

# s1 - s2; set subtraction
print(s1 - s2)

# exclusive value that only have in on set
print(s1 ^ s2)

#list converted in set and remove duplicate value
li = [1,2,3,4,2,3,5,6,3]
print(li)
s = set(li)
print(s)
#li = list(s)
# li = list(set(i)) doesn't work for a reason
