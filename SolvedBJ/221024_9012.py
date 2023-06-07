from sys import stdin

for _ in range(int(stdin.readline())):
    open = 0
    for i in stdin.readline().rstrip():
        open += 1 if i == "(" else -1
        if open < 0:
            print("NO")
            break
    else:
        print("YES" if open == 0 else "NO")
