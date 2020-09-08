file = open("cd6.txt", "w")
# when file exists, it opens, else it creates in the current directory (if not specified)
for i in range(12):
    file.write(str(i) + "\n")  # only string type can be written to files
file.close()

file = open("cd6.txt", "a")
charlist = []
for k in range(1, 40, 3):
    charlist.append('*' * k + "\n")
file.writelines(charlist)
file.close()

file = open("cd6.txt", "r")
print(file.read())
file.close()
