from collections import defaultdict as ddict

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
        
        
        
        
        
#         min_left, min_right = (-1, m + 1)

#         # left 0 잡고 right를 한 칸 씩 옮겨가며 탐색
#         left = 0
#         for right, ss in enumerate(s):
#             # s의 현재 character가 t를 커버하기 위해 아직 필요하다면 remain 줄이기
#             if count[ss] > 0:
#                 remain -= 1
#             count[ss] -= 1  # count에서는 항상 감소

#             # remain이 0 -> 후보 window 등장
#             if remain == 0:
#                 # 왼쪽을 줄이기
#                 while True:
#                     left_ch = s[left]
#                     if count[left_ch] == 0:
#                         # 이 경우는 더 이상 줄일 수 없는 거니까 break
#                         break
#                     count[left_ch] += 1
#                     left += 1
                
#                 # 현재 후보가 기존 후보보다 작은 window라면 갱신
#                 if right - left < min_left - min_right:
#                     min_left, min_right = (left, right)
                
#                 # for문을 이어나가기 위한 정리
#                 count[s[left]] += 1
#                 remain += 1
#                 left += 1
        
#         # right가 갱신이 안됐다 == 불가능하다
#         if min_right > m:
#             return ""
#         return s[min_left:min_right + 1]

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 길이 계산
        m = len(s)
        n = len(t)

        # Ex 3: t가 더 길면 애초에 성립하지 않음
        if n > m:
            return ""
        
        # 현재 t를 커버하기 위해 남아 있는 character count
        count = ddict(lambda: 0)
        for tt in t:
            count[tt] += 1
        
        # t를 커버하기 위해 필요한 남은 character 전체 개수
        remain = n
        # 구하는 게 최소 window 사이즈니까 어떻게 잡는 게 최소가 될지를 구함
        min_left = -1
        min_right = m + 1

        start_index = 0
        for end_index, ch in enumerate(s):
            if count[ch] > 0:
                remain -= 1
            count[ch] -= 1

            if remain == 0:
                while True:
                    char_at_start = s[start_index]
                    if count[char_at_start] == 0:
                        break
                    count[char_at_start] += 1
                    start_index += 1
                
                if end_index - start_index < min_right - min_left:
                    min_left = start_index
                    min_right = end_index
                
                count[s[start_index]] += 1
                remain += 1
                start_index += 1
        
        return "" if min_right > m else s[min_left:min_right + 1]