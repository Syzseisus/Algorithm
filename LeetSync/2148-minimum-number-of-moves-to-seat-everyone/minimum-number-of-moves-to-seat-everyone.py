from collections import Counter, deque

# class Solution:
#     def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
#         # 가능한 의자 찾기
#         seats = Counter(seats)

#         # 학생 정렬하고 탐색
#         students.sort()
#         answer = 0
#         for s in students:
#             # 자기와 가장 가까운 
#             min_pos = min(seats)
#             if (s in seats) and (seats[s] > 0):
#                 seats[s] -= 1
#                 if seats[s] == 0:
#                     del seats[s]
#                     if not seats:
#                         break
#             else:
#                 answer += abs(min_pos - s)
#                 seats[min_pos] -= 1
#                 if seats[min_pos] == 0:
#                     del seats[min_pos]
#                     if not seats:
#                         break

#         return answer


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # 의자 정렬
        seats.sort()
        seats = deque(seats)

        # 학생 정렬하고 탐색
        students.sort()
        answer = 0
        for s in students:
            curr_seat = seats.popleft()
            answer += abs(curr_seat - s)

        return answer
