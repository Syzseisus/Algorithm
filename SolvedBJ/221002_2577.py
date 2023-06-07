A = int(input())
B = int(input())
C = int(input())

cal = str(A * B * C)
# print(cal, type(cal))
for i in '0123456789':
    print(cal.count(i))