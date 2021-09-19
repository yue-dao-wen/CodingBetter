# -*- coding: utf-8 -*-
"""
@author: Me
@time: 2021/9/8 23:08
@description:
"""
from typing import List
import heapq


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        pairs = [(speed[i], efficiency[i]) for i in range(n)]
        pairs.sort(key=lambda x:x[1])

        # 最大的ef 最大的sepeed

        ans = 0


        for _ in range(k):

            pass






        pass


def main():
    pass


if __name__ == "__main__":
    main()
