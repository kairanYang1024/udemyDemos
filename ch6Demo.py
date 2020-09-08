# dictionaries
# keys and values pair (= map in java/c++)
import random as rnd

people = {"John": 32, "James": 20}  # use : to separate key/values
print(people["John"])  # access value by key instead of index

numbers = {
    1: "one",
    2: "two",
    3: "three",
    4: "four"
}
print(1 in numbers)  # check if 1 exists in numbers
print(5 in numbers)  # check if 5 exists in numbers -- false
print("three" in numbers)  # can also check values
# print(numbers[5]) # KeyError
print(numbers.get(5))  # None
print(numbers.get(5, "key not found"))
print(list(numbers.items()))  # returns a list containing tuple for k-v pairs
print(list(numbers.keys()))  # returns a list of keys in numbers
print(list(numbers.values()))  # returns a list of values in numbers
numbers.popitem()  # removes the last inserted element
print(list(numbers.items()))
numbers.pop(3)
print(list(numbers.items()))

x = ("a", "b", "c", "d", "e", "f")
y = [1, 2, 3]
mydict = numbers.fromkeys(x, y)
print(numbers)  # not modified
print(mydict)  # new dictionary created, from tuple so order is not preserved

x = list(x)
for ascii in range(103, 123):
    x.append(chr(ascii))  # ascii to char

for i in range(100):
    x.append(chr(rnd.randint(97, 122)))

countFreq = {}
for letter in x:
    if letter not in countFreq:
        countFreq.setdefault(letter, 1)
    else:
        countFreq.update({letter: countFreq[letter] + 1})
print(countFreq)

# sort a dictionary:
# 3.6+: {k, v for k, v in sorted(countFreq.items(), key = lambda item: item[1])}
# 3.5-:
import operator

countFreq = sorted(countFreq.items(), key=operator.itemgetter(1), reverse=True)
# by value = 1, by key = 0; reverse=True descending, False ascending
print(countFreq)
del x, countFreq, y, people, numbers, mydict

# tuples (immutable ds)
fruits = ("apple", "pear", "mango", "grape", "apple")
print(fruits)
print(fruits[0])
# fruits[0] = "pineapple"  # TypeError: does not support item assignment
print(fruits.count("apple"))  # returns frequency of that elem
print(fruits.index("pear"))  # returns the index of that elem, if multiple, idx of its first occurrence

# list slicing
numbers = list(range(100, 1001, 100))
print(numbers[2:5])
print(numbers[2:8:2])
print(numbers[-8:-2])
print(numbers[-2:-8:-1])  # descending
print(numbers[-2::-1])  # descending
print(numbers[:4:2])  # ascending from beginning
print(numbers[:-4])  # ascending from beginning to -4 (4th last)
print(numbers[:-4:-1])  # descending from beginning to -4 (backward)

# list comprehension
squares = [x ** 2 for x in range(0, 100)]  # squares of 0 # ~ 100
print(squares)
squares = [x ** 2 for x in range(0, 100) if x ** 2 % 2 == 0]  # even squares by inserting conditionals
print(squares)
print(len(squares))  # bcz odd number square is odd number
squares.remove(256)  # remove a specified element in the list
print(squares)
# squares.remove(2) # if not found? ValueError
squares.pop(5)  # remove the element at specified index in the list
print(squares)
squares.pop(-1)  # negative indices also work, but not overflowing indices
# squares.pop(55) #IndexError
print(squares)


# sort a list
def sortingCriteria(x):
    return x / 10 + x % 10

squares.sort(key=sortingCriteria, reverse=True)
# descending by last digit & number magnitude
print(squares)
del fruits, numbers, squares

# string formatting
numbers = [4,5,6]
numberstring = "Numbers:{0},{1},{2}".format(numbers[0], numbers[1], numbers[2])
# {0}, {1}, {2} are number holders (index holders)
print(numberstring)

a = "{x}/{y}".format(x=100, y=300)  # for x, y {vars}, need specify instead of ordinal
print(a)

# string functions
print(",".join(["Apple", "Banana", "Citrus"]))  # defines the separator joining list of strings
print("Hello There".replace("There", "Man"))  # replace one substring by another
newstring = "Gestalt"
print(newstring.replace("alt", "malt"))
print(newstring.replace("alv", "malt")) #if substring not found --> replace failed, use original

newstring = "This is a string"
print(newstring.startswith("there")) #false
print(newstring.endswith("ing")) #true
print(newstring.split(" ")) #split by delimeter " "

# numeric functions (besides numpy)
import math  # this entire module is kinda inferior to numpy
print(min(3,1,2,4,9)) #can have min multiple arguments
print(max(3,1,2,4,9))
print(abs(-1.114514))
print(math.gcd(278, 156))
print(math.fsum([1,4,3.5,2.8,4.9]))
print(math.sin(3.14159/2))
print(math.sin(math.radians(30)))  # precision is low
print(math.exp(10))