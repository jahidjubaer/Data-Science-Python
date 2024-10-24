def multiplaction_table(n):
  for i in range(1, 11):
    print("{} {} = {}".format(n , i , n * i))

n = int(input("Enter a number while n == 0"))
while n != 0:
  multiplaction_table(n)
  n = int(input("Enter a number while n == 0"))