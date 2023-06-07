import sys

A, B, C = map(int, sys.stdin.readline().strip().split())

# library
answer = pow(A, B, C)

# # Divide and Conquer
# # 0, 홀, 짝으로 나눔
# # 나누는 위치 주의
# def DC(A, B, C):
#     if B == 0:
#         return 1

#     temp = DC(A, B // 2, C) % C
#     temp = (temp * temp) % C
#     if B & 1:
#         temp = (temp * A) % C
    
#     return temp

# answer = DC(A, B, C)

print(answer)