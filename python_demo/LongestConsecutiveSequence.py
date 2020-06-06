# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def longestConsecutive_unionfind(self, nums: List[int]) -> int:
        dict_root = {}
        def find(m):
            if m not in dict_root:
                return m
            else:
                dict_root[m] = find(dict_root[m])
            return dict_root[m]
        for n in nums:
            dict_root[n] = n + 1
        longest = 0
        for n in nums:
            reach = find(n + 1)
            longest = max(longest, reach - n)
        return longest

    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for n in nums:
            if n - 1 in set_nums:
                continue
            m = n + 1
            while m in set_nums:
                m += 1
            longest = max(longest, m - n)
        return longest

if __name__ == '__main__':
    sol = Solution()
    # nums = [1,111,22,1,3,2]
    nums = [-4,-1,4,-5,1,-6,9,-6,0,2,2,7,0,9,-3,8,9,-2,-6,5,0,3,4,-2]
    print(sol.longestConsecutive_unionfind(nums))