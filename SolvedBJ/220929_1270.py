from collections import defaultdict

# def help(arr):
#     count = defaultdict(lambda: 0)
#     for i in arr:
#         count[i] += 1
#         if count[i] > len(arr) // 2:
#             return i
#     return 'SYJKGW'

def Boyer_Moore(n, arr):
    '''
    1. count가 0일 때 현재 값을 major로 설정
    2. major와 현재 값이 같으면 count += 1, 아니면 -= 1
    '''
    count = 0
    major = 0
    for num in arr:
        if count == 0:
            major = num
        count += 1 if major == num else -1
    
    # count가 0이 아니면 major의 가능성이 있다.
    if count:
        # 그러나 위 방식 만으로는 같을 때, 딱 절반일 때를 거르지 못함
        # 따라서 major가 되기 위한 절반 값을 설정하고
        major_cnt = n // 2
        for num in arr:
            # major가 몇 개인지 센다
            if num == major:
                major_cnt -= 1
            # major가 과반수보다 많으면 major
            if major_cnt < 0:
                return major

    return 'SYJKGW'

N = int(input())
for _ in range(N):
    arr = list(map(int, input().strip().split()))
    print(Boyer_Moore(arr[0], arr[1:]))