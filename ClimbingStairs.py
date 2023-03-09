class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second =1
        temp = 0
        if n == 1:
            temp = 1
        else:
            
            while n-1:
                temp = first + second
                second = first
                first = temp
                n -= 1
                
        return temp