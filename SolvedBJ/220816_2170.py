import sys
from collections import deque

inp = lambda: sys.stdin.readline()

def main():
    N = int(inp())
    lines = []

    for _ in range(N):
        s, e = map(int, inp().split())
        lines.append((s, e))

    # s 순으로 정렬됨
    lines.sort()
    lines = deque(lines)
    left, right = lines.popleft()
    answer = right - left

    while lines:
        s, e = lines.popleft()
        # 포함되는 경우
        # left <= s가 필요하지만 이미 정렬됨
        if e <= right:
            continue

        # 일단 늘리고
        answer += e - s
        
        # 겹치는 부분 빼기
        # e <= right와 겹치는 부분을 빼야한다.
        # 하지만 첫 if보다 strict한 조건을 걸었기 때문에
        # 그 겹치는 부분은 이미 첫 if에서 걸러졌다.
        if s < right:
            answer -= right - s
        
        left = s
        right = e

    print(answer)

if __name__ == "__main__":
    main()