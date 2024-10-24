#capitalize len
color = ['red', 'green', 'blue', 'black']
cap = [item.capitalize() for item in color]
print(cap)

#len of each color
length = [len(item) + 3 for item in color]
print(length)

#add
add = [item + 3 for item in length]
print(add)


#range
li = [x*x*x for x in range(2, 10)]
print(li)

#condition
li = [x*x for x in range(2, 20) if x % 2 == 0]
print(li)