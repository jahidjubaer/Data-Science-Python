#user input
# input() take input as string : so we need to type cast in int
marks = input("Enter your number !")
print(type(marks))
marks = int(marks)

#conditional operation
if marks >= 40:
  print("congratulations Your passed")
else :
  print("Hard luck! you failed !")



#GPA

marks = int(input("Enter your Number : "))
if marks >= 80:
  print("Your GPA: A+")
elif marks >= 70:
  print("Your GPA: A")
elif marks >= 60:
  print("Your GPA: B")
elif marks >= 50:
  print("Your GPA: C")
else :
  print("You are failed in exam")

print("done XD")


#n is positive or negative and odd or even

n = int(input("Enter the number: "))

if n >= 0 and n % 2 == 0 :
  print(n, "is positive and even number!")
elif n < 0 and n % 2 == 0:
  print(n, "is negative number and even number!")
elif n >= 0 and n % 2 == 1:
  print(n, "is positive and odd number")
else :
  print(n, "is negative number and odd number")


#leap year

year = int(input("Year : "))

if year % 100 == 0 and year % 400 == 0 :
  print(year, "is leap year!")
elif year % 4 == 0 and year % 100 != 0 :
  print(year, "is leap year!")
else :
  print(year, "is not a leap year!")



