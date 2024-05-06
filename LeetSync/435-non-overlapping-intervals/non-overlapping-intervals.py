class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        
        answer = 0
        end = -65535
        for left, right in intervals:
            if left >= end:
                end = right
            else:
                answer += 1

        return answer