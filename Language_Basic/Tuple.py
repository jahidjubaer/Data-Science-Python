list = [3,35,2,6,3]
print(list)
tl = (5,3,2,5,6)
print(tl)
print(type(tl))

#tuple is immutable
list[0] = 5
print(list)

#but for tuple there generate a error
# tuple [0] = 5 #here generate a error
print(tuple)

tpl = 4,3,5,2,3,5
print(tpl, type(tpl))

#print tuple using for loop
for i in tpl :
  print(i)

#tuple function
print(dir(tuple))

tple = 3,4,3,4,5 # its like a pack
print(tple)
a, b, c, d,e = tple # value of tple assign in a, b, c, d, e
print(a, b, c, d,e)
