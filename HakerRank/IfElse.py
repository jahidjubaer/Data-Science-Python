n = int(input())

if n % 2 == 1 :
    print("Weird\n")
elif n % 2 == 0 :
    if 2 <= n <= 5 :
        print("Not Weird\n")
    elif 6 <= n <= 20 :
        print("Weird\n")
    elif n > 20 :
        print("Not Weird\n")

