class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        answer = 0
        end = 0
        intervals.sort(key=lambda x: (x[0], -x[1]))
        for _, e in intervals:
            if e > end:
                answer += 1
                end = e
        return answer