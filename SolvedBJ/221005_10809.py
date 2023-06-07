from collections import defaultdict

s = input().strip()
pos = defaultdict(lambda: -1)
for i in range(len(s) - 1, -1, -1):
    pos[s[i]] = i

print(*list(pos[i] for i in 'abcdefghijklmnopqrstuvwxyz'))