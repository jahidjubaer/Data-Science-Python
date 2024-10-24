li = {4, 5, 2, 7, 8, 9, 10}

#value in list
found = 15 in li
print(found)

#in linear
key = 11
flag = True
for i in li :
    print(i)
    if i == key:
        flag = False
        print("found")
        break
if flag :
    print("NOt found")