# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        row = len(matrix)
        col = len(matrix[0])
        row_limit = [0, row-1]
        col_limit = [0, col-1]
        while row_limit[0] <= row_limit[1] and col_limit[0] <= col_limit[1]:
            if row_limit[0] == row_limit[1]:
                for c in range(col_limit[0], col_limit[1] + 1):
                    res.append(matrix[row_limit[0]][c])
                break
            if col_limit[0] == col_limit[1]:
                for r in range(row_limit[0], row_limit[1] + 1):
                    res.append(matrix[row_limit[r]][col_limit[0]])
                break
            for c in range(col_limit[0], col_limit[1]):
                res.append(matrix[row_limit[0]][c])
            for r in range(row_limit[0], row_limit[1]):
                res.append(matrix[r][col_limit[1]])
            for c in range(col_limit[1], col_limit[0], -1):
                res.append(matrix[row_limit[1]][c])
            for r in range(row_limit[1], row_limit[0], -1):
                res.append(matrix[r][col_limit[0]])
            col_limit[0] += 1
            col_limit[1] -= 1
            row_limit[0] += 1
            row_limit[1] -= 1
        return res

if __name__ == '__main__':
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # matrix = [[1,2,3]]
    matrix = [1,2,3]
    if type(matrix[0]) == int:
        print()
    sol = Solution()
    sol.spiralOrder(matrix)
