s = 'abcdefg'
print(type(s))

#concatinate
print('10' + '10')
print('Bangladesh ' * 5)
print('4 ' * 10)

#len
print(len(s))

#acessing by index
print(s[1:5]) #print bcde
print(s[:]) #print full string
print(s[-1]) #print the last value of string
print(s[-2:]) #print last two value of string
print(s[0]) #print 0 index value
print(s[1]) # print first index value

#upper case and lower case
name = 'jahid'
name = name.upper()
print(name)
print(name.lower())
print(name.capitalize())

#find substring
c = "Bangladesh"
print(c.find("Bangla")) #give output by index
print(c.find("desh"))
print(c.find('cccc'))

#endwith , startwith
print(c.startswith("Bangla"))
print(c.endswith("desh"))
print(c.endswith("hi"))

#split and join
s = "a,b,c,d,e"
print(s.split(','))
list = ['d', 'a', 'd', 'g']
print("".join(list))


