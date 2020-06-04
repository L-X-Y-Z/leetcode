# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        left = [1] * len_nums

        for i in range(1,len_nums):
            left[i] = left[i-1] * nums[i-1]
        # right = [1] * len_nums
        # for i in range(-2, -len_nums-1, -1):
        #     right[i] = right[i+1] * nums[i+1]
        # return [x*y for x,y in zip(left,right)]
        right_product = 1
        for i in reversed(range(len_nums)):
            left[i] *= right_product
            right_product *= nums[i]
        return left
if __name__ == '__main__':
    nums = [1,2,3,4]
    sol = Solution()
    print(sol.productExceptSelf(nums))