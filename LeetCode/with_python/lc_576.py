# -*- coding: utf-8 -*-
"""
@author: Me
@time: 2021/8/15 23:53
@description:
"""


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # 广度优先遍历
        # x或者y触到边界【0, n-1】就计数
        # 有没有不用把所有路径都记录下来的方法？

        x_hit_edge = lambda x: x == 0 or x == m - 1
        y_hit_edge = lambda y: y == 0 or y == n - 1

        seen = set()
        n_cross = 0

        def bfs(x, y, n_left):
            nonlocal n_cross
            if x < 0 or x >= m or y < 0 or y >= n or n_left < 1:
                return
            # if (x, y) in seen:
            #     return
            if x == 0:
                n_cross += 1
            if x == m - 1:
                n_cross += 1
            if y == 0:
                n_cross += 1
            if y == n - 1:
                n_cross += 1
            # if x_hit_edge(x) and y_hit_edge(y):
            #     n_cross += 2
            # elif x_hit_edge(x) or y_hit_edge:
            #     n_cross += 1
            # seen.add((x, y))
            bfs(x - 1, y, n_left - 1)
            bfs(x + 1, y, n_left - 1)
            bfs(x, y - 1, n_left - 1)
            bfs(x, y + 1, n_left - 1)

        bfs(startRow, startColumn, maxMove)

        return n_cross % (10 ** 9 + 7)


def main():
    sl = Solution()
    # m = 2
    # n = 2
    # maxMove = 2
    # startRow = 0
    # startColumn = 0

    m = 1
    n = 3
    maxMove = 3
    startRow = 0
    startColumn = 1

    print(sl.findPaths(m, n, maxMove, startRow, startColumn))

    pass


if __name__ == "__main__":
    main()
