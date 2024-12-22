# https://leetcode.com/problems/house-robber/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        
        for i, n in enumerate(nums):
            if i == 0:
                dp[i] = n
            elif i == 1:
                dp[i] = max(n, dp[i - 1])
            else:
                dp[i] = max(n + dp[i - 2], dp[i - 1])
            
        return max(dp)

