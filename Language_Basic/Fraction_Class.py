# a / b
# numerator / denominator
#to use gcd function have to import math
import math
class Fraction:
    def __init__(self, n , d):
        self.numerator = n
        self.denominator = d

    def __str__(self):
        return  "{} / {}".format(self.numerator, self.denominator)

    #method for add fraction
    #here self work for f1 function and f work for f2 function
    def add(self, f):
        g = math.lcm(self.denominator, f.denominator )
        num = g / self.denominator * self.numerator + g/ f.denominator * f.numerator
        self.numerator =  int (num)
        self.denominator = g

    #oparetor overloading '+'
    #we can also overload '-', '*' '/' by __sub__ , __mul__ , __div__ magic method
    def __add__(self, f):
        g = math.lcm(self.denominator, f.denominator)
        num = g / self.denominator * self.numerator + g / f.denominator * f.numerator
        return  Fraction(int (num), g)

# __str__ , __init__, __add__ are magical method / function

f1 = Fraction(3, 4)
print(f1) # output : 3 / 4

f2 = Fraction(4, 10)

f1.add(f2)
# the added value store in f1
print(f1) # output : 23 / 24

#using operator overloading
print(f1 + f2)
# for only answer
result = f1 + f2
print(result.numerator , result.denominator)