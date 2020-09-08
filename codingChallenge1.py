p = input("Enter value for p (principal value): \n")
n = input("Enter value for n (number of years): \n")
r = input("Enter value for r (rate of interest): \n")

# convert string to int, since input() stores info in string
p = int(p)  # defensive? if p is other string literals?
n = int(n)
r = float(r)

si = (p * n * r) / 100
print("simple interest is ", si)
