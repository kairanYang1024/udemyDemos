# errors and exceptions

# syntax error: incorrect syntax for a line of code
# will be caught by IDE (pycharm, intellij, eclipse)
#def func1(a, b) <missing colon>
#    print(a + b)
#func1(2, 4)

# logical error: not getting desired value (bugs) by logical mistakes impl by programmers
# i.e. not meeting specifications

# exceptions: don't allow code to run for them
def div(a, b):
    return a/b

print(div(3,0.001)) #0) # zero-division error (exception)

# exception handling

# try-except (= java try-catch)
def div(a, b):
    try:
        print(a/b)
    except ZeroDivisionError:  # if we catched a line of code that invokes divZeroError:
        print("You are dividing a number by 0")

div(3, 5)
div(3, 0)

# try-except-finally
# finally: executed no matter what (independent from the exception caught)
try:
    a = 20
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("You are diving a number by 0")
finally:
    print("Hit endline")

# file handing
file = open("demo.txt", 'r')
# w = write file mode, write content not read it
# r = read file mode
content = file.read() # read all content of the file
print(content)
file.close()

file = open("demo.txt", 'r')
content = file.read(10) # read first 10 bytes of the file
print(content)
file.close()

file = open("demo.txt", 'r')
content = file.readline() # read a line of the file, input confines how many bits are read from this line
print(content)
file.close()

file = open("demo.txt", 'r')
content = file.readlines(43)
# read lines of the file, return as a list of strings
# input confines the maximal bits read from the text
# but if exceeds one byte then the entire line after is read
print(content)
file.close()

file = open("demo.txt", 'w')  # open the file in write mode, clears the content before
file.write("New line only\n")
file.close()
file = open("demo.txt", 'r')
content = file.read()  # read only the content written by 'w'
print(content)
file.close()

file = open("demo.txt", 'a')  # append mode, will not clear the content written before
file.write("I love you\n")  # append only 1 line
file.close()

file = open("demo.txt", 'a')
# file.writelines(["I feel so unsure\n", "As I take your hand\n", "and lead you to the dancefloor\n"])
# appends multiple lines as a list, need \n
# or:
lyrics = ["I feel so unsure\n", "As I take your hand\n", "and lead you to the dancefloor\n"]
file.writelines(lyrics[:2])
file.close()





