# -*- coding: utf-8 -*-
class Solution:
    def lengthOfLongestSubstring_1(self, s:str) -> int:
        set_repeat = set()
        longest = 0
        end = -1
        for i in range(len(s)):
            if s[i] in set_repeat:
                set_repeat.remove(s[i])
            while end + 1 < len(s) and s[end+1] not in set_repeat:
                set_repeat.add(s[end+1])
                end += 1
            longest = max(longest, end-i+1)
        return longest

    def lengthOfLongestSubstring(self, s:str) -> int:
        set_repeat = set()
        longest = 0
        start = -1
        for i in range(len(s)):
            if s[i] in set_repeat:
                while s[start + 1] != s[i]:
                    set_repeat.remove(s[start + 1])
                    start += 1
                start += 1
            else:
                set_repeat.add(s[i])
            longest = max(longest, i - start)
        return longest


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abbbbbbbbbbbbbbb"))
