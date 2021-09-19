# -*- coding: utf-8 -*-
"""
@author: Me
@time: 2021/9/15 23:02
@description:
"""

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int], ) -> int:
        # 二分法
        n = len(nums)
        left, right = 0, n - 1

        def get_value(idx):
            return nums[idx] if 0 <= idx < n else float('-inf')

        ans = -1
        while left <= right:
            mid = (right + left) // 2
            if get_value(mid - 1) < get_value(mid) > get_value(mid + 1):
                ans = mid
                break
            if get_value(mid) < get_value(mid + 1):
                left = mid + 1
            else:
                right = mid - 1

        return ans


# 用栈


def main():
    sl = Solution()
    exmples = [
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [4, 3, 2, 3, 4],
        [0],
        [1, 2],
        [1, 3, 2],
        [1, 2, 3, 4, 2],
    ]

    for nums in exmples:
        print(sl.findPeakElement(nums))

    pass


if __name__ == "__main__":
    main()
