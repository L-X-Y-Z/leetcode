# -*- coding: utf-8 -*-
class Solution:
    def reach(self, s, center, touch):
        while center - touch >= 0 and center + touch < len(s) and s[center - touch] == s[center + touch]:
            touch += 1
        return touch - 1

    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 2:
            return s
        s = '#' + '#'.join(s) + '#'
        len_s = len(s)
        res = None
        longest_center = 0
        farthest_reach_center = 0
        radius = [0] * len_s
        for i in range(len_s):
            horizon = farthest_reach_center + radius[farthest_reach_center]
            if i <= horizon:
                if radius[farthest_reach_center - (i - farthest_reach_center)] + i < horizon:
                    radius[i] = radius[farthest_reach_center - (i - farthest_reach_center)]
                else:
                    radius[i] = self.reach(s, i, horizon - i)
                    farthest_reach_center = i
            else:
                radius[i] = radius[i] = self.reach(s, i, 1)
                farthest_reach_center = i
            if radius[i] >= radius[longest_center]:
                res = s[i - radius[i]: i + radius[i] + 1]
                longest_center = i
        return res.replace('#', '')

if __name__ == '__main__':
    print(len("ffffffffff"))
    print(len("bbbbbbbbbb"))
    sol = Solution()
    s = 'bbbbbb'
    print(len(s))
    res = sol.longestPalindrome(s)
    print(len(res))
