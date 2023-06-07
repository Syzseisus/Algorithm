'''
이면수: 5 제외 4 이상의 수, 각 자리수 합 홀수
임현수: 4 or 2 or 소인수 개수 짝수 개
성경수: 이면수도, 임현수도 아님
* 이면수이면서 임현수일 수 있음
'''

import sys
from math import sqrt, ceil

def factorization(n, primes):
    if n == 1:
        return primes

    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            primes.add(i)
            break
    else:
        primes.add(n)
        return primes
    
    return factorization(n // i, primes)

def is_imyeon(n):
    if n in ['1', '2', '3', '5']:
        return 0
    
    return sum([int(i) for i in n]) % 2

def is_imhyeon(n):
    if n in ['2', '4']:
        return 1
    elif n == '1':
        return 0
    
    n = int(n)
    primes = set()
    primes = factorization(n, primes)

    return 1 - (len(primes) % 2)

def is_sk(n):
    imyeon = is_imyeon(n)
    imhyeon = is_imhyeon(n)
    if not imyeon and not imhyeon:
        return True
    else:
        return False

def is_both(n):
    imyeon = is_imyeon(n)
    imhyeon = is_imhyeon(n)
    if imyeon and imhyeon:
        return True
    else:
        return False


N = sys.stdin.readline().strip()
check = is_imyeon(N) + 2 * is_imhyeon(N)
check = 4 if check == 3 else 3 if check == 0 else check
print(check)

'''
IM IH -> out
 0  0      3 = 1*0 + 2*0 = 0 -> 3
 0  1      2 = 1*0 + 2*1
 1  0      1 = 1*1 + 2*0
 1  1      4 = 1*1 + 2*1 = 3 -> 4
'''