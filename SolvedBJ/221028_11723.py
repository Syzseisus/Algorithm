from sys import stdin

# S = set()
S = 2 ** 20

def operation(op, x, S):
    if op == 'add':
        # S.add(int(x))
        S |= (1 << int(x))
    elif op == 'remove':
        # S.discard(int(x))
        S &= ~(1 << int(x))
    elif op == 'check':
        # print(1 if int(x) in S else 0)
        check = (1 << int(x)) & S
        print(1 if check else 0)
    elif op == 'toggle':
        # if int(x) in S:
        #     S.discard(int(x))
        # else:
        #     S.add(int(x))
        x = (1 << int(x))
        if S & x:
            S &= ~x
        else:
            S |= x
    elif op == 'all':
        # S = set(range(1, 21))
        S = 2 ** 21 - 1
    elif op == 'empty':
        # S = set()
        S = 0

    return S


for _ in range(int(stdin.readline())):
    op = stdin.readline().rstrip().split()
    S = operation(op[0], op[-1], S)
