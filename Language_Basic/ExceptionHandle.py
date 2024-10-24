try:
    fp = open('myfile.txt', 'r')
    view = fp.read()
    print(fp)

except FileNotFoundError:
    print("This file is not found")

while True:
    number1 = int(input("Number1 :"))
    number2 =int(input("Number2 : "))
    if number2 == 0 and number1 == 0:
        break
    try:
        print(number1 / number2)
    except ZeroDivisionError:
        print("can't divided by zero")
