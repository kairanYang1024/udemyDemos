def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Dividing by zero, please retry")
        return 0  # default return value


x = float(input("Enter the first number: \n"))
y = float(input("Enter the second number: \n"))
print(divide(x, y))

