class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea_Val = 0
        l,r = 0, len(height) - 1
        while l < r:
            tempArea = abs(l-r) * min(height[l],height[r])
            maxArea_Val = max(maxArea_Val,tempArea)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return maxArea_Val