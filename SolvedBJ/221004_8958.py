T = int(input())

def grading(case):
    score = 0

    curr = 0
    for i in case:
        if i == "O":
            curr += 1
            score += curr
        else:
            curr = 0
    
    print(score)

for _ in range(T):
    case = input().strip()
    grading(case)