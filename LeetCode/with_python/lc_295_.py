# -*- coding: utf-8 -*-
"""
@author: Me
@time: 2021/8/28 10:08
@description:
"""


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.l_idx = 0
        self.r_idx = 0
        self.count = 0

    def insert_2(self, num, left, right):
        while left <= right:
            mid = (left + right) // 2
            if self.nums[mid] == num:
                self.nums = self.nums[:mid] + [num] + self.nums[mid:]
                return
            elif self.nums[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        self.nums = self.nums[:right + 1] + [num] + self.nums[right + 1:]

    def addNum(self, num: int) -> None:

        if self.count == 0:
            self.nums.append(num)
            self.count += 1
            return

        if self.count & 1 == 1:
            if num >= self.nums[self.r_idx]:
                self.insert_2(num, self.r_idx, len(self.nums) - 1)
                self.r_idx += 1
            elif num < self.nums[self.l_idx]:
                self.insert_2(num, 0, self.l_idx)
                self.r_idx += 1
        elif self.count & 1 == 0:
            if num >= self.nums[self.r_idx]:
                self.insert_2(num, self.r_idx, len(self.nums) - 1)
                self.l_idx += 1
            elif num < self.nums[self.l_idx]:
                self.insert_2(num, 0, self.l_idx)
                self.l_idx += 1
            elif self.nums[self.l_idx] <= num < self.nums[self.r_idx]:
                self.nums = self.nums[:self.l_idx + 1] + [num] + self.nums[self.r_idx:]
                self.l_idx += 1
        self.count += 1

        pass

    def findMedian(self) -> float:
        return self.nums[self.l_idx] if self.count & 1 == 1 else (self.nums[self.l_idx] + self.nums[self.r_idx]) / 2
        pass


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


def main():
    ops = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    nums = [[], [1], [2], [], [3], []]
    sl = None
    for idx, op in enumerate(ops):
        if op == 'MedianFinder':
            sl = MedianFinder()
        elif op == "addNum":
            sl.addNum(nums[idx][0])
        elif op == "findMedian":
            print(sl.findMedian())
    pass


if __name__ == "__main__":
    main()
