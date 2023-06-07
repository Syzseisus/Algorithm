'''
finger:  1  2  3  4  5
number:  1  2  3  4  5
         9  8  7  6
           10 11 12 13
        17 16 15 14
           18 19 20 21

따라서
엄지: 8 x usable
소지: 8 x usable + 4
기타: 4 x usable + 1 + (4 - hurt) if usable % 2 else (hurt - 2)
'''

import sys

hurt = int(sys.stdin.readline())
usable = int(sys.stdin.readline())

answer = 0
count = 0
if usable == 0:
    answer = hurt - 1
else: 
    if (hurt == 1) or (hurt == 5):
        answer += (8 * usable) + (hurt - 1)
    else:
        answer += (4 * usable) + 1
        answer += (4 - hurt) if usable % 2 else (hurt - 2)

print(answer)