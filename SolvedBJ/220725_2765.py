# 1 mile = 5280 feet
# 1 foot = 12 inch
# 1 perlong = 201.168 meter

import sys

pi = 3.1415927
N = 1
while True:
    D, R, T = map(float, sys.stdin.readline().split())
    if not R:
        break

    circum = pi * D
    miles = circum * R / (12 * 5280)

    T /= 60 * 60
    mph = miles / T

    print(f"Trip #{N}: {miles:.2f} {mph:.2f}")
    N += 1
