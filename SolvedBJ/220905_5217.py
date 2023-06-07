import sys

inp = lambda: int(sys.stdin.readline())

def get_pairs(n):
    left = 1
    right = n - 1
    queue = []
    while left < right:
        queue.append((left, right))
        left += 1
        right -= 1
    
    return queue   


N = inp()
for _ in range(N):
    target = inp()
    queue = get_pairs(target)

    print(f"Pairs for {target}: ", end='')
    if queue:
        for i in range(len(queue)):
            if i:
                print(", ", end='')
            pair = queue[i]
            print(f"{pair[0]} {pair[1]}", end='')
    print()
