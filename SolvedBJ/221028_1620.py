from sys import stdin

'''
번호: 1 ~ N
이름: 처음만 대문자 or 마지막만 대문자, 2 ~ 20글자
     -> lower
알파벳(이름) -> 해당 번호
숫자(번호) -> 해당 이름
'''

N, M = map(int, stdin.readline().split())
num_to_name = {i: stdin.readline().rstrip() for i in range(1, N + 1)}
name_to_num = {v: k for k, v in num_to_name.items()}

# print(num_to_name.values())
# print(name_to_num.values())

for _ in range(M):
    given = stdin.readline().rstrip()
    if given.isdigit():
        print(num_to_name[int(given)])
    else:
        print(name_to_num[given])