# -*- coding: utf-8 -*-
import copy
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        if not s or not words:
            return res
        len_w = len(words[0])
        len_words = len(words)
        len_total = len_w * len_words
        dict_word_count = {}
        for w in words:
            dict_word_count[w] = dict_word_count.get(w, 0) + 1
        for i in range(len(s) - len_total + 1):
            dict_copy = copy.deepcopy(dict_word_count)
            j = 0
            while j < len_total:
                w_cur = s[i+j:i+j+len_w]
                if w_cur not in dict_copy:
                    break
                if dict_copy[w_cur] < 1:
                    break
                dict_copy[w_cur] -= 1
                j += len_w
            if j == len_total:
                res.append(i)
        return res

    def findSubstring_bruteforce(self, s: str, words: List[str]) -> List[int]:
        res = []
        if not s or not words:
            return res
        len_w = len(words[0])
        len_words = len(words)
        total_len = len_w * len_words
        standard = ''.join(sorted(words))
        for i in range(len(s) - total_len + 1):
            substring = s[i:i+total_len]
            parts = sorted([substring[idx: idx+len_w] for idx in range(0, total_len, len_w)])
            if ''.join(parts) == standard:
                res.append(i)
        return res

if __name__ == '__main__':
    sol = Solution()
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print(sol.findSubstring(s, words))