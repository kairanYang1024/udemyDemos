# function arguments & return
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

m = 2
n = 9.21
q = add(m, n)
s = add(str(m), "hello")
t = multiply(m, q)
u = multiply(s, 3)
print(q)
print(s)
print(t)
print(u)
del m, n, q, s, t, u

def makeList(n, type):
    ret = []
    if type.lower() == 'string':
        ret.append("hello")
        ret.append(" ")
        ret.append("world!")
    elif type.lower() == 'int':
        for x in range(n):
            ret.append(x)
    elif type.lower() == 'float' or type.lower() == 'double':
        for x in range(1, n):
            ret.append(x / 100)
    elif type.lower() == 'boolean' or type.lower() == 'bool':
        ret.append(True)
        ret.append(False)
    else:
        print("Type not recognized")
    return ret

print(makeList(100, "double"))
print(makeList(10, "int"))
print(makeList(10, "string"))
print(makeList(10, "bool"))

def retMultiple(x, y):
    sum = x+y
    diff = x-y
    prod = x*y
    return sum, diff, prod

s, _, _ = retMultiple(3, 4)  # use _ to ignore the return value
tup = retMultiple(4, 5) # this time returns a tuple for unpacking
print(s)
print(tup)
s, *notUsed = retMultiple(3, 9)  # use * + <var_name> to specify the unpacking var is a list
print(type(notUsed))
s, *_ = retMultiple(12, 7.392)
print(s)
del s, _, tup, notUsed

# pass func as argument of another func, inside, horizontal, outside order
def square(c):
    return c * c

result = square(add(2, 3))
print(result)
del result

# module = set of code and can be used in our code, equivalent to java package, c++ library
import random as rand
for x in range(5):
    result = rand.randint(1, 6)
    print(result)


