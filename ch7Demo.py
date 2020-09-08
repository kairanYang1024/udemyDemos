# functional programming
# code written in functions, solve task in series of functions
# passing one function as argument to other functions

def add_ten(x):
    return x + 10  # add 10 to the input


def cube(x):
    return x ** 3


def twice(func, arg):  # pass the function (name) as an argument
    return func(func(arg))  # f^2(x)


print(twice(add_ten, 230))  # this semantic actually works, but only of scope 1 arguments

# lambdas
print(cube(4))  # regular call-in functions
result = (lambda x: x ** 3)(20)  # lambda defines a function (similar to inline in c++)
print(result)
print((lambda x: x ** 3)(20))


# equivalent to anonymous function, automatically returns the statement
# is an expression and has value

# map: perform operations on (the entire) lists, = linear mapping for finite sets
def add(x):
    return x + 2


newlist = [10, 20, 30, 40, 50]
result_list = list(map(add, newlist))  # apply the add function to the entire list
print(result_list)
print(map(add, newlist))  # map object, printing its pointer

result_list = list(map(lambda x: x ** 3, newlist))  # can also use lambda shorthands
print(result_list)
del newlist, result_list

# filter: used with lambdas to filter out a particular list
newlist = [i for i in range(1, 400) if i % 7 == 0]  # already one criteria presented here
result = list(filter(lambda x: x % 4 == 0, newlist))  # filter by criteria
print(result)


# generator: similar to lists, can iterate by for-loop but not supporting index
# created by functions and yieid statements
def function():
    counter = 0
    while counter < 5:
        yield counter  # generate a sequence
        counter += 1


for x in function():  # print the generators, can be accessed by outside code
    print(x)


def seven(x):
    for i in range(x):
        if i % 7 == 0:
            yield i


print(list(seven(100)))
