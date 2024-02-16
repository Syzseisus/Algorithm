class Solution:
    def maxArea(self, height):
        lb = 0
        ub = len(height) - 1
        
        Area = 0
        
        while lb < ub:
            temp = (ub-lb) * min(height[lb], height[ub])
            if height[lb] < height[ub]:
                lb += 1
            else:
                ub -= 1
                
            Area = max(Area, temp)        
        
        return Area