'''
[100 26 13 17 24 33 100 99]
[ 34 56 21  1 24 34 100 99]
100, 34 -> hp가 0 이하가 되므로 패스

26, 56  -> O
        13, 21  -> O
                17, 1   -> O
                        24, 24  -> O
                                33, 34  -> hp가 0 이하가 되므로 패스
                                100, 100-> hp가 0 이하가 되므로 패스
                                99, 99  -> hp가 0 이하가 되므로 패스
                                최종: 56 + 21 + 1 + 24 = 102
                                -> X
                                33, 34  -> O
                                        100, 100-> hp가 0 이하가 되므로 패스
                                        99, 99  -> hp가 0 이하가 되므로 패스
                                        최종: 56 + 21 + 1 + 34 = 112
                                        -> X
                                        100, 100-> hp가 0 이하가 되므로 패스
                                        99, 99  -> hp가 0 이하가 되므로 패스
                                        최종: 56 + 21 + 1 = 78
                        -> X
                        24, 24  -> O
                                33, 34  -> O
                                        100, 100-> hp가 0 이하가 되므로 패스
                                        99, 99  -> hp가 0 이하가 되므로 패스
                                        최종: 56 + 21 + 24 + 34 = 135
                                        -> X
                                        100, 100-> hp가 0 이하가 되므로 패스
                                        99, 99  -> hp가 0 이하가 되므로 패스
                                        최종: 56 + 21 + 24 = 101
                                -> X
                                33, 34  -> O
                                        100, 100-> hp가 0 이하가 되므로 패스
                                        99, 99  -> hp가 0 이하가 되므로 패스
                                        최종: 56 + 21 + 34 = 111
                                        -> X
                                        100, 100-> hp가 0 이하가 되므로 패스
                                        99, 99  -> hp가 0 이하가 되므로 패스
                                        최종: 56 + 21 = 77
                -> X ...
        -> X ...
        ...
그니까,,
하나 씩 빼서
걔를 썼을 때 / 안 썼을 때 중에 최댓값이 될 때를 저장
'''

import sys

inp = lambda: sys.stdin.readline()

N = int(inp())

hp = list(map(int, inp().strip().split()))
joy = list(map(int, inp().strip().split()))

def help(prev_hp, prev_joy, i):
    # 전부 탐색하면 joy 반환
    if i == N:
        return prev_joy
    
    # i번째 사람이랑 hp 깍고
    curr_hp = prev_hp - hp[i]
    # 0 이하가 되면 i번째 건너 뛰고 다음으로 넘어감
    if curr_hp <= 0:
        return help(prev_hp, prev_joy, i + 1)

    # 아니면 joy 늘림
    else:
        curr_joy = prev_joy + joy[i]
        
        # 그렇게 i번째를 만난 거랑
        do_use = help(curr_hp, curr_joy, i + 1)
        # 가능하지만 그냥 넘기고 간 거랑
        dont_use = help(prev_hp, prev_joy, i + 1)
        # 둘 중에 최댓값 반환
        return max(do_use, dont_use)

print(help(100, 0, 0))