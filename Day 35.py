import math
class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2**31 - 1 
        min_int = -2**31
        res = 0  
        while x:
            rem = int(math.fmod(x, 10)) 
            x = int(x / 10) 
            if (res > max_int // 10 or (res == max_int // 10 and rem >= max_int % 10)):
                return 0
            if (res < min_int // 10 or (res == min_int // 10 and rem <= min_int % 10)):
                return 0 
            res = (res * 10) + rem 
        return res
solution = Solution()
result = solution.reverse(123)
print(result)
