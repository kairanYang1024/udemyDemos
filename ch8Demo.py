class Teddy:
    quantity = 200  # class attribute, created to every object same (static in java)

    # use constructor to define instance attribute of the class
    def __init__(self, name, color):
        self.name = name
        self.color = color  # assign the instance attribute from parameter
        # instance attributes are created at runtime, and defined for init
        # constructor overload (function overload): use default argument for short

    def whiten(self):
        self.color = "White"  # modifies instance attributes (by indicating .)
        print("Method called")

    def change_color(self, new_color):
        self.color = new_color


# teddy1 = Teddy() # invoke default constructor (overwritten when init defined)
teddy1 = Teddy("Ted", "blue")
print(teddy1)  # memory location and trace on files
print(teddy1.quantity)
print(teddy1.name)
print(teddy1.color)

teddy2 = Teddy("Rob", "brown")
print(teddy2.name)
print(teddy2.color)
teddy2.whiten()
print(teddy2.color)
teddy2.change_color("Yellow")
print(teddy2.color)


# OOP vs functional: OOP we create everything in objects!

class Student:

    def __init__(self, name="John", age=15):  # having default arguments
        self.name = name
        self.age = age
        # can also have starred *args, **kwargs to represent many attributes
        # (overloading for every)

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.age = new_age

    def set_name(self, new_name):
        self.name = new_name


student1 = Student("James", 18)
print(student1.get_name())
print(student1.get_age())
name = input("Rename yourself to \n")
student1.set_name(name)
print(student1.get_name())

# Inheritance
class ScienceStudent(Student):  # equivalent to java extends, c++ (:)
    def science(self):
        print("Veritas")

student2 = ScienceStudent("Jason", 19)
print(student2.get_age())
print(student2.science())

# because of python dynamic type binding, there's no real sense of polymorphism,
# just base/derived class using its overloaded method versions

# multiple inheritance

class Rectangle:
    def __init__(self, width=1, height=1, color="white"):
        self.width = width
        self.height = height
        self.color = color

    def get_color(self):
        return self.color

    def get_area(self):
        return abs(self.width) * abs(self.height)


class Paintable:
    def __init__(self, area_cost = 100, time_cost = 50):
        self.area_cost = area_cost
        self.time_cost = time_cost

    def get_area_cost(self):
        return self.area_cost

    def get_time_cost(self):
        return self.time_cost

    def delayPainting(self):
        self.time_cost += 20


class PaintGrid(Rectangle, Paintable): # inherits from multiple classes (supported in C++ --> possible error, not supported in java)
    def __init__(self, width=1, height=1, color="white",
                 area_cost = 100, time_cost = 50):
        # a way to combine the attributes of the 2 base classes
        Rectangle.__init__(self, width, height, color)  # multiple base, called respective
        Paintable.__init__(self, area_cost, time_cost)  # if inherits from one just call super().__init__

    def get_total_cost(self):
        return self.area_cost * self.get_area() + self.get_time_cost()

    def change_color(self, new_color):
        self.color = new_color
        self.time_cost += 10


myGrid = PaintGrid(20, 99, "yellow")
myGrid.delayPainting()
print("unit cost: ", myGrid.get_area_cost())
print("area: ", myGrid.get_area())
print("time cost: ", myGrid.get_time_cost())
print("total cost: ", myGrid.get_total_cost())


# Recursion
def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # called itself inside function


print(fibonacci(7))
print(fibonacci(2))
print(fibonacci(11))


# Set (Data Structure)
numset = {1,2,3,4,5,6}  # same {} as dictionary but only 1 entry
print(numset)
print(5 in numset)
numset.remove(2) # O(1) rmv
print(numset)
numset.add(9)
print(numset)
numset.pop() # pops the first elem in set
print(numset)

numshet = {3, 5, 7, 9, 11}
intrsct = numset.intersection(numshet)  # like an overloading binary op
unon = numset.union(numshet) # same symmetric
diff = numset.difference(numshet)
print(intrsct)
print(unon)
print(diff)
print(numset | numshet) # short-hand for union, overloading op
print(numset & numshet) # short-hand for intersection, overloading op
print(numset - numshet) # short-hand for difference, overloading op
# symmetric difference, shorthand ^, equiv to XOR in logic operations

# Itertools: preloaded in modules, helping iterables (iterators in java/c++)
from itertools import count
for i in count(3):
    print(i) # keep on counting till infinity
    if i >= 20:
        break

from itertools import accumulate, takewhile
numbers = list(accumulate(range(8)))
print(numbers)  # 0, 1+0, 2+1, 3+2+1, 4+3+2+1,... till sum(8)
# a way to do prefix sum/max/min in python

print(list(takewhile(lambda x: x<= 6, numbers)))
# only the satisfied condition will be printed
# similar to list comprehension/filter


# Operator Overloading (+, -, *, /, |, &, ^...)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # overloading + operator
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y) # create the sum object

    def __str__(self):  # equiv to java tostring, c++ '<<'
        return "({0},{1})".format(self.x, self.y)

p1 = Point(1, 4)
p2 = Point(2, 5)
p3 = p1 + p2
print(p3)


# Data Hiding/Encapsulation
# only certain amt of code is exposing to (outside the class), user input
class Myclass:
    __hidden = 0 # private member in Java/C++, use __ (double underscore)
    def add(self, increment):
        self.__hidden += increment
        print(self.__hidden)

s = Myclass()
s.add(10)
# print(s.__hidden)  # Attribute Error: only useable inside the class
