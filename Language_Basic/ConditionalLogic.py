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

