# PSUEDO-Random Number Generator
# Linear Congruential Generator

def lcg(seed, m, c, a):
    count = 1
    xn = seed
    while count != 100:
        xn = (((xn * a) + c) % m)
        count += 1
        print(xn)

seed = int(input("seed: "))
m = int(input("m input: "))
c = int(input("c input: "))
a = int(input("a input: "))

print(lcg(seed, m, c, a))
