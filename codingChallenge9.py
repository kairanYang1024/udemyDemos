def student_discount(price):
    return price * 0.9  # 10% discount


def regular_coupon(price):
    return price * 0.95 # 5% discount


def simult(disc_mode1, disc_mode2, price):
    return disc_mode1(disc_mode2(price)) # apply both simultaneously


price = int(input("Enter the price for applying coupon: \n"))
coupon1 = eval(input("Enter the first coupon you have: \n").lower())  # input func name
coupon2 = eval(input("Enter the second coupon you have: \n").lower())
# eval can have error if the string inputted is not matched the name of function
print("The price after discount is ", simult(coupon1, coupon2, price))