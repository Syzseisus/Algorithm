while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    
    longest = max(a, b, c)
    if 2 * (longest ** 2) == a ** 2 + b ** 2 + c ** 2:
        print('right')
    else:
        print('wrong')