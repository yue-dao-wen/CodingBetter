# -*- coding: utf-8 -*-
"""
@author: Me
@time: 2021/8/24 22:54
@description:
"""
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        # row 和 col有什么讲究？谁横谁竖着？
        cost = [[float('inf')] * n for _ in range(k+2)] # 什么时候+1？
        # 纵是几次航班，横是目的地
        # cost[1][2] 表示乘坐1次航班到2号地所需要的花费
        # cost[0][src] = 0 ，表示乘坐0次航班到源目的地的花费是0,
        cost[0][src] = 0
        for t in range(1, k+2):
            # 乘坐t次航班可以到的地方
            for j, i, c in flights:
                # 乘坐t次航班可以到i的价钱 = 乘坐t-1次航班到上一个地方j所需的钱 + 上一个地方到这个地方的钱
                cost[t][i] = min(cost[t][i], cost[t-1][j] + c)

        # 可以走1次到，也可以走2次到，选那个花费最少的。其中花费是无穷的，意思是走这么多次，根本到不了
        ans = min(cost[t][dst] for t in range(1, k + 2))
        return -1 if ans == float('inf') else ans



    def findCheapestPrice_bfs(self, n, flights, src, dst, k):
        # 广度优先？
        # 三色避免重复？
        # 动态规划？
        to_dict = defaultdict(list)
        for f in flights:
            to_dict[f[0]].append((f[1], f[2]))

        seen_citys = [0] * n
        memo = {}

        def helper(idx, kk):
            # 步数没有了
            # 到目的地了
            # 这个城市来过了
            if idx == dst:
                # 到了
                return 0
            if kk < 0:
                return float("inf")
            if seen_citys[idx] == 1:
                return float("inf")
            if (idx, kk) in memo:
                return memo[(idx, kk)]

            seen_citys[idx] = 1     # 通常这种应该放在哪里？
            res = float("inf")
            for t, p in to_dict[idx]:
                res = min(helper(t, kk - 1) + p, res)
            seen_citys[idx] = 0
            memo[(idx, kk)] = res

            return res

        res = helper(src, k)
        if res == float("inf"):
            res = -1
        return res


def main():
    sl = Solution()
    n = 3
    edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    k = 1

    n = 5
    edges = [[0, 1, 100], [0, 2, 100], [0, 3, 10], [1, 2, 100], [1, 4, 10], [2, 1, 10], [2, 3, 100], [2, 4, 100],
             [3, 2, 10],
             [3, 4, 100]]
    src = 0
    dst = 4
    k = 3

    print(sl.findCheapestPrice(n, edges, src, dst, k))

    pass


if __name__ == "__main__":
    main()
