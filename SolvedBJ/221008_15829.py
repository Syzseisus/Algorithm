alpha = 'abcdefghijklmnopqrstuvwxyz'
hashdic = {k: v for v, k in enumerate(alpha, 1)}

N = int(input())
s = input()
ans = sum(hashdic[s[i]] * (31 ** i) for i in range(N))
print(ans % 1234567891)