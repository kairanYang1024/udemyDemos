# if statement
age = int(input("enter your age\n"))
if age >= 21:  # remember this (:) instead of () {} in java/c++
    print("You may drink alcohol\n")
else:
    print("You cannot drink alcohol\n")
# indentation is extremely important in python

marks = int(input('Enter your marks: \n'))

if marks >= 90:
    print("Amazing!")
elif marks >= 70:
    print("Compatible")
elif marks >= 50:
    print("Despicable!")
else:
    print("Failing")

# list
names = ["Mike", "John", "Samuel", "Lorra", "Irina"]
print(names)  # print the entire list
print(names[0])  # access element
print(names[1:4])  # access segment (sublist, last excluded)
name = names[4]
name = "Rein"  # relocated away from names[4]
print(names)
names[4] = "Rein"  # modifies the list
print(names)

numbers = [1, 1, 1, 1, 1]
numbers[2] = 7  # assigned successfully
print(numbers)

newNumbers = [2, 2, 2, 2, 2]
print(numbers + newNumbers)  # concatenating lists
print(newNumbers * 3)  # overloading * to ints

fruits = ["Apple", "Mango", "Peach"]
print("Apple" in fruits)  # hasElement operation
print("Orange" in fruits)
# fruits[3] index error
fruits.append("Orange")  # insert "Orange" at end of list
fruits.insert(1, "Grape")  # insert "Grape" at index 1
print(fruits)
print(len(fruits))  # fruits.size() in C++ vector/java list, fruits.length in java array
print(fruits.index("Peach"))  # index of an element in the list
# print(fruits.index("Banana"))  # not in list element? error

# range()
numbers = list(range(10))  # list function makes a list
print(numbers)
numbers = list(range(3, 8))  # start, end
print(numbers)
numbers = list(range(3, 30, 5))  # start, end, step
print(numbers)


# code reuse & functions
def foo1():
    print("1")
    print("New York")
    print("MEME")


foo1()  # function call must be after function definition (or included in module)
foo1()

# for loops
for x in range(1, 11, 2):  # for(x = 1; x < 11; x+=2) in java/c++
    print("my name is ")
    print(x//2)

for fruit in fruits:  # for-each loop to access list/tuple/dictionaries
    print(fruit)

# boolean logics
username = "admin"
password = "admin123"
if username == 'admin' and password == "admin123":
    print("success!")
else:
    print("failed to login.")
# keyword for logic operators in python: and, or, not instead &&, ||, !

# while loop semantics
counter = 0
while counter < 10:
    print(counter)
    counter += 1

