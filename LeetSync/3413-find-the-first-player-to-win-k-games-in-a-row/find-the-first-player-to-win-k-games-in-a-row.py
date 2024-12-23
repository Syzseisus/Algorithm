# class Solution:
#     def findWinningPlayer(self, skills: List[int], k: int) -> int:
#         n = len(skills)
#         # k 조정
#         #   - 전체 리스트를 다 보고 나면 이길 애는 skill level 제일 높은 애임
#         k = min(k, n - 1)
        
#         # 첫 번째 있는 애 (i)를 기준으로 계산
#         win = 0
#         i = 0
#         for j in range(1, n):
#             # 지면 i를 바꿔치고, 이전 i를 이겼으니까 win = 1
#             if skills[i] < skills[j]:
#                 i = j
#                 win = 1
#             # 이기면 win만 올리기
#             else:
#                 win += 1
#             # 정해진 횟수를 채웠다면 거기서 종료, 첫 번째 애가 정답
#             if win == k:
#                 break
        
#         # 아까 조정했던 거처럼, 전체 리스트 다 보고 나면 (for 문 끝나면)
#         # 첫 번째에는 skill level이 제일 높은 애가 있고, 걔가 정답
#         return i


from collections import deque
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        players = {s: i for i, s in enumerate(skills)}
        k = min(k, len(skills))
        queue = deque(skills)
        win = 0
        a = queue.popleft()
        while win != k:
            b = queue.popleft()
            if a > b:
                win += 1
                queue.append(b)
            elif b > a:
                win = 1
                a, b = b, a
                queue.append(b)
        
        return players[a]