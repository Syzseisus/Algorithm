# Customer Per Officer
# 해당 시간 동안 전체 심사관이 맡을 수 있는 사람 수 return
def cpo(guess, times):
    cnt = 0
    for time in times:
        cnt += guess // time    # 해당 시간 동안 심사관 한 명이 맡을 수 있는 사람 수
    return cnt

def solution(n, times):
    lb = 1                  # Lower Bound
    ub = min(times) * n     # Upper Bound = 혼자서 n명 다 하는 거
    
    while lb <= ub:
        guess = (lb + ub) // 2      # lb와 ub 중간값으로 추정
        if cpo(guess, times) >= n:  # 1. 추정 값에 대한 return이 n 이상: 시간이 충분함
            answer = guess          #    -> 일단 답으로 저장하고
            ub = guess - 1          #       그보다 낮은 값으로도 가능할지 확인 (ub 내림)
        else:                       # 2. n 미만: 시간이 부족함
            lb = guess + 1          #    -> lb 올림

    return answer

# 테스트 1 〉	통과 (0.01ms, 10.2MB)
# 테스트 2 〉	통과 (0.06ms, 10.1MB)
# 테스트 3 〉	통과 (3.59ms, 10.2MB)
# 테스트 4 〉	통과 (126.81ms, 14.2MB)
# 테스트 5 〉	통과 (402.56ms, 14.1MB)
# 테스트 6 〉	통과 (259.76ms, 14.1MB)
# 테스트 7 〉	통과 (364.31ms, 14.1MB)
# 테스트 8 〉	통과 (501.65ms, 13.9MB)
# 테스트 9 〉	통과 (0.02ms, 10MB)
