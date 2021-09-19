# -*- coding: utf-8 -*-
"""
@author: Me
@time: 2021/9/8 22:16
@description:
"""
import heapq
from typing import List


class Solution:

    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]):
        # TODO: 贪心算法到底是啥？
        # todo: 为啥用堆呢？
        if w > max(capital):
            return w + sum(heapq.nlargest(k, profits))  # todo: nlargest的源代码

        n = len(capital)

        cps = [(capital[i], profits[i]) for i in range(n)]
        cps.sort(key=lambda x: x[0])

        able_list = []
        idx = 0
        for _ in range(k):
            while idx < n and cps[idx][0] <= w:
                heapq.heappush(able_list, -cps[idx][1])
                idx += 1

            if able_list:
                w -= heapq.heappop(able_list)
            else:
                break

        return w

        # 每一次找有条件限制下的最大值。
        # 从capital里找profits最大的值。这个过程怎么找是最快的？
        # 以profits为权重，


def main():
    sl = Solution()
    k = 2
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 1]

    k = 3
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 2]

    print(sl.findMaximizedCapital(k, w, profits, capital))


    pass


if __name__ == "__main__":
    main()
