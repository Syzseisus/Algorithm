class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set([n])
        curr = sum(int(i) ** 2 for i in str(n))
        while curr != 1:
            if curr in visited:
                return False
            visited.add(curr)
            curr = sum(int(i) ** 2 for i in str(curr))
        return True