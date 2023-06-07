import sys

A = int(sys.stdin.readline())
B = sys.stdin.readline().strip()

three = A * int(B[2])
four = A * int(B[1])
five = A * int(B[0])
sum = three + four * 10 + five * 100

print(three)
print(four)
print(five)
print(sum)
