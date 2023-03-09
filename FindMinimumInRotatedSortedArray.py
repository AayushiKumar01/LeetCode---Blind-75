class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l,r = 0,len(nums)-1
        min_val = float("infinity")
        while l <= r:
            mid = (l+r) // 2
            
            if nums[r] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
            
            min_val = min(nums[mid],min_val)
            
        return min_val
            