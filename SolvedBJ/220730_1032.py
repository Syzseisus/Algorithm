import sys

inp = lambda: sys.stdin.readline()

N = int(inp())
pattern = inp().strip()
length = len(pattern)
for _ in range(N - 1):
    fn = inp().strip()
    temp = []
    for i in range(length):
        if pattern[i] == "?":
            temp.append(pattern[i])
        elif pattern[i] == fn[i]:
            temp.append(pattern[i])
        else:
            temp.append("?")
    pattern = "".join(temp)

print(pattern)
