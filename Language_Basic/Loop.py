n = int(input("enter your number: "))

for i in range(1, n + 1, 1):
    print(i)
print("")
for i in range(n  , 0, -1):
    print(i)


#sum of 1 to k number using function
def add(k) :
    sum = 0
    for i in range(1, k + 1, 1):
        sum += i
    return sum

k = int(input())
print(add(k))


#multipliction table
def multipliction_table(n) :
  for i in range(1, 11):
    #print(n," X ", i ," = ", n * i)
    #using formating
    print("{} x {} = {}".format(n, i, n * i))

n = int(input("input your number : "))
for i in range(1, n + 1):
  multipliction_table(i)
  print(" ")