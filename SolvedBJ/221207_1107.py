from sys import stdin


def main():
    target = int(stdin.readline())
    num_broken = int(stdin.readline())
    broken = stdin.readline().split()

    if target == 100:
        return 0

    if num_broken == 0:
        if target == 99:
            return 1
        elif target == 101:
            return 1
        elif target == 102:
            return 2
        else:
            return len(str(target))
    else:
        answer = abs(100 - target)

        if num_broken != 10:
            for num in range(1000001):
                num = str(num)
                for d in num:
                    if d in broken:
                        break
                else:
                    answer = min(answer, abs(int(num) - target) + len(num))

        return answer

print(main())
