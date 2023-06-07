from sys import stdin

while True:
    line = stdin.readline().rstrip()
    if line == ".":
        break
    stack = []
    for i in line:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if not stack or stack[-1] == "[":
                print("no")
                break
            elif stack[-1] == "(":
                stack.pop()
        elif i == "]":
            if not stack or stack[-1] == "(":
                print("no")
                break
            elif stack[-1] == "[":
                stack.pop()
    else:
        print("no" if stack else "yes")
