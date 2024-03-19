class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        answer = 0
        end = 0
        intervals.sort(key=lambda x: (x[0], -x[1]))
        for _, e in intervals:
            answer += e > end
            end = max(end, e)
        return answer