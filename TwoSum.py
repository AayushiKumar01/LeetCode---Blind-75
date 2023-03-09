class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index in range(len(nums)):
            diff = target - nums[index]
            if diff in hashmap:
                return [index, hashmap[diff]]
            hashmap[nums[index]] = index