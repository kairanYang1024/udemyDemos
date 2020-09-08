class WeirdNumber:
    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        x = self.x + other.x
        return x

a = WeirdNumber(2)
b = WeirdNumber(3)
print(a*b)