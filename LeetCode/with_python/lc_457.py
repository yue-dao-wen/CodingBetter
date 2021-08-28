# -*- coding: utf-8 -*-
"""
@author: Me
@time: 2021/8/7 23:20
@description:
"""

from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # 还是个三色问题？
        n = len(nums)
        colors = [0] * n

        def has_circle(idx):
            if colors[idx] > 0:
                return colors[idx] == 2
            colors[idx] = 1

            next_idx = idx + nums[idx]
            next_idx %= n
            next_has = has_circle(next_idx)
            if next_has:
                colors[idx] = 2

            return next_has

        for i in range(n):
            if has_circle(i):
                return True

        return False


def main():
    sl = Solution()
    nums = [2, -1, 1, 2, 2]
    print(sl.circularArrayLoop(nums))
    pass


if __name__ == "__main__":
    main()
