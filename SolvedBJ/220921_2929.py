import sys

order = sys.stdin.readline().strip()

indices = [i for i in range(len(order)) if order[i].isupper()]
answer = 0
for i, ind in enumerate(indices):
    if ind % 4:
        _, r = divmod(ind, 4)
        r = 4 - r
        answer += r
        for j in range(i, len(indices)):
            indices[j] += r
print(answer)