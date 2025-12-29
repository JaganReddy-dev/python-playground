def karatsuba(x: int, y: int) -> int:
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    power = 10**m
    a = x // power
    b = x % power
    c = y // power
    d = y % power

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
    return (10 ** (2 * m) * ac) + (10**m) * ad_plus_bc + bd


print(karatsuba(1234, 5678))
