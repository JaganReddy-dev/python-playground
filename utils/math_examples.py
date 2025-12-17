import math


def math_examples():
    sqrt = math.sqrt(16)
    fac4 = math.factorial(4)
    print(f"sqrt: {sqrt}")
    print(fac4)
    # decimal comparision using math.isclose()
    deciimalCompare = math.isclose((0.1 + 0.2 + 0.1), 0.6)
    print(f"decimal comparision: {deciimalCompare}")
    # understanding arithmetics and return data types
    print(5 / 3)
    print(1.5**2)
    print(type(1.5**2))
    # checking if two variables are equal using is
    x = 1.2
    y = 1.2
    print(f"is: {x is y}")
