from collections import Counter

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = Counter(seats)
        students.sort()
        answer = 0
        for s in students:
            min_pos = min(seats)
            if (s in seats) and (seats[s] > 0):
                seats[s] -= 1
                if seats[s] == 0:
                    del seats[s]
                    if not seats:
                        break
            else:
                answer += abs(min_pos - s)
                seats[min_pos] -= 1
                if seats[min_pos] == 0:
                    del seats[min_pos]
                    if not seats:
                        break

        return answer
