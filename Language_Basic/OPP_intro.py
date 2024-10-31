class car:
    make = 'Toyota'

    def __init__(self, mk, md1, year):
        self.made = mk
        self.model = md1
        self.year = year

    def horn(self):
        print("Beep beep bep!")

    def move(self):
        print("car is moving")

#to access this class
print(car.make)
#car.move()

#making a instance or object
my_class = car('toyota', 'to40', 2013)
print(my_class.make)

# 0 positional arguments but 1 was given
# print(my_class.move())
#it will not run , but if we move(self) add argument it will run
my_class.move()
#for 'self' argument it will pass the object 'my_class'

#make a new object or car class named "mycar"
my_car = car('Tesla', 't200', 2016)
my_car.horn()

#print toyota for my_class.made and print tesla for my_car.made
print(my_class.made, my_car.made)