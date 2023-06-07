A, B = map(int, input().strip().split())

answer = '>' if A > B else '==' if A == B else '<'
print(answer)