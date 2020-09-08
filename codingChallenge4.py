def calculateBMI(height, weight):
    return weight / (height ** 2)


myHeight = float(input("Enter your height in meters: \n"))
myWeight = float(input("Enter your weight in kilograms: \n"))
print(calculateBMI(myHeight, myWeight))
