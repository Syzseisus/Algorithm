class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
#         n = len(values)
#         if n == 2:
#             return sum(values) - 1

#         answer = 0
#         max_rewarded = values[0] + 0
#         for i in range(1, n):
#             v = values[i]
#             penalted = v - i
#             answer = max(answer, max_rewarded + penalted)
#             rewarded = v + i
#             max_rewarded = max(max_rewarded, rewarded)

#         return answer

        n = len(values)
        answer = 0
        max_rewarded = values[0] + 0
        for i in range(1, n):
            v = values[i]
            penalted = v - i
            answer = max(answer, max_rewarded + penalted)
            rewarded = v + i
            max_rewarded = max(max_rewarded, rewarded)
        
        return answer