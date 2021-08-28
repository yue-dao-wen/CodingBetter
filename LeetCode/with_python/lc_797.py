# -*- coding: utf-8 -*-
"""
@author: Me
@time: 2021/8/25 23:21
@description:
"""

from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(graph)

        def backtrack(idx, lujing):
            if idx == n - 1:
                ans.append(lujing[:])
                return
            for next_id in graph[idx]:
                backtrack(next_id, lujing + [next_id])


        backtrack(0, [0])

        return ans

        pass


def main():
    sl = Solution()
    graph = [[1, 2], [3], [3], []]
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    graph = [[1], []]
    graph = [[1, 2, 3], [2], [3], []]
    graph = [[1, 3], [2], [3], []]
    graph = [[], [], []]
    print(sl.allPathsSourceTarget(graph))

    pass


if __name__ == "__main__":
    main()
