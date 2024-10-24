key_value = dict()

key_value[1] = "one"
key_value[2] = "two"
key_value[3] = "three"
key_value[4] = "Five"
print(key_value)

key_value2  = {1 : "one is fire", 2 : "two is oon", 3 : "three is gone"}
print(key_value2)

#print by index
print(key_value[3])

#delete a key_pair
del key_value2[1]
print(key_value2)

#print using loop
for i in key_value2 :
  print(key_value2[i])

#print key and value using loop
for ke, value in key_value2.items() :
  print(ke,"=", value)

#function in dictionary
#print(dir(key_value2))

#key value print
print(key_value2.items())


furits =    {'a' : 'apple', 'b' : 'banana', 'c' : 'cat' , 'm' : 'mango' }
print (furits.keys())

#if the key doesnt exits it make error
print(furits['c'])
#but get doesnt make error it print none
print(furits.get('c'))
