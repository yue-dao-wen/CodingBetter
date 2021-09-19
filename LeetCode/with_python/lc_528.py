# -*- coding: utf-8 -*-
"""
@author: Me
@time: 2021/8/30 22:25
@description:
"""

import random
from bisect import bisect_left
from itertools import accumulate
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.pre = list(self.accumulate(w))
        self.total = sum(w)

    def accumulate(self, w):
        ans = [0] * len(w)
        for i in range(1, len(w)):
            ans[i] = w[i - 1] + ans[i - 1]
        return ans

    def bisect_left(self, nums, val, lo=0, hi=None):
        if hi is None:
            hi = len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < val:
                lo = mid + 1
            else:
                hi = mid
        return lo


    def pickIndex(self) -> int:
        x = random.randint(1, self.total)
        return self.bisect_left(self.pre, x)


def main():
    pass


if __name__ == "__main__":
    main()
