from sys import stdin

'''
4, 3, 6, 8, 7, 5, 2, 1
4를 위해서 "4"번 push 힌 번 pop
3은 stack 맨 마지막이니까 pop
6을 위해서 "(6-4)"번 push 한 번 pop
8을 위해서 "(8-6)"번 push 한 번 pop
7은 stack 맨 마지막이니까 pop
남은 stack 세 개, 남은 개수 세 개, 따라서 세 번 pop

1, 2, 5, 3, 4
1을 위해서 "1"번 push 한 번 pop
2를 위해서 "(2-1)"번 push 한 번 pop
5를 위해서 "(5-2)"번 push 한 번 pop
3을 위해서 "(3-5)"번..? --> NO
'''

def main():
    stack = []
    answer = []
    count = 1
    flag = True
    for i in range(int(stdin.readline())):
        num = int(input())
        while count <= num:
            stack.append(count)
            answer.append('+')
            count += 1

        if stack[-1] == num:
            stack.pop()
            answer.append('-')
        else:
            flag = False

    if flag:
        print(*answer, sep='\n')
    else:
        print("NO")

if __name__ == "__main__":
    main()
