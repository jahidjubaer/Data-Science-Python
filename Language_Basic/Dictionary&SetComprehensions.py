#Dictonary Comprehensions
list = [(1, 'one'), (5, 'five'), (6,'six')]
de = {v:k for v,k in list}
print(de)

de = {v: k for k, v in list}
print(de)

#Set comprehensions

s = 'abcdefadfdge'
u_value = {value for value in s}
print(u_value)
print(type(u_value)) #set
print(type(de)) #dict


#mixed
list = [('messi', 'red'), ('naymer', 'blue'), ('rakib', 'blue'), ('musa', 'green')]
print(list)
dt = {name : color for name, color in list}
print(dt)

color_value = {col for col in dt.values()}
print(color_value)

