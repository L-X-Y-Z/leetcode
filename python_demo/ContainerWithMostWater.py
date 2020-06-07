# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        capacity = 0
        left = 0
        right = len(height) - 1
        while left < right:
            capacity = max(capacity, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return capacity

if __name__ == '__main__':
    sol = Solution()
    # height = [1,8,6,2,5,4,8,3,7]
    height = [1,2,1]
    print(sol.maxArea(height))
