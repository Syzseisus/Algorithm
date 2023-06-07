from sys import stdin
from collections import deque

def reverse(arr):
    return arr[::-1]

def delete(arr):
    return 

def main():
    func = stdin.readline().rstrip()
    N = int(stdin.readline())
    arr = deque(stdin.readline().strip('[,]\n').split(','))

    if func.count('D') > N:
        print('error')
        return

    left = True
    for token in func:
        if token == 'R':
            left = not left
        elif token == 'D':
            try:
                if left:
                    arr.popleft()
                else:
                    arr.pop()
            except:
                print('error')
                return
        else:
            print('error')
            return
    if arr == ['']:
        print('error')
        return
    
    if left:
        print("[", ','.join(arr), "]", sep='')
    else:
        answer = '['
        for i in range(len(arr)-1, 0, -1):
            answer += arr[i] + ','
        answer += arr[0] + ']'
        print(answer)


T = int(stdin.readline())
for _ in range(T):
    main()