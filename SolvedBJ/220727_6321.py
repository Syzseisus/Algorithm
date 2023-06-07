import sys

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    inp = sys.stdin.readline().strip()
    oup = "".join([chr(ord(x) + 1) if x != "Z" else "A" for x in inp])
    print(f"String #{i}\n", oup, sep="")
    if i != N:
        print()
