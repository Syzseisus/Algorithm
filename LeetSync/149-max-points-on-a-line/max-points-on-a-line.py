from collections import defaultdict

class Solution:
    def maxPoints(self, points):
        # 예외처리: 점이 두 개 이하면 그게 답임
        if len(points) <= 2:
            return len(points)
        
        ans = 0
        lines = defaultdict(set)
        for i, point1 in enumerate(points):
            for point2 in points[i+1:]:
                if point1[0] == point2[0]:
                    slope = None
                    intercept = point1[0]
                else:
                    slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
                    intercept = point1[1] - slope * point1[0]
                lines[(slope, intercept)].add(tuple(point1))
                lines[(slope, intercept)].add(tuple(point2))
        
        for line in lines:
            ans = max(len(lines[line]), ans)

        return ans