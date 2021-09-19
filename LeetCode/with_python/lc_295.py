# -*- coding: utf-8 -*-
"""
@author: Me
@time: 2021/8/27 22:56
@description:
"""

import heapq


class MyMinHeap:
    def __init__(self):
        self.nums = []
        #
        # TODO: 自己实现一个堆
        # TODO： 堆其实就是一个按照某种奇怪的方式排列的数组，进行排列就行。
        # TODO: 堆排序可以，一个一个添加的时候，怎么实时的去上浮和下潜？ heapify里面就有这个过程啊！！

    def siftdown(self):
        # TODO： 为啥叫做siftdown？ 这是不是向上吗？
        new = self.nums[-1]
        idx = len(self.nums) - 1
        while idx > 0:
            parent_idx = (idx - 1) >> 1
            parent = self.nums[parent_idx]
            if new < parent:
                self.nums[idx] = parent
                idx = parent
                continue
            break
        # TODO: 为啥不需要考虑同一阶层的另一个子节点？
        self.nums[idx] = new
        pass

    # todo： 确定了最大堆还是最小堆之后，代码的哪些地方不同？

    # todo: 同一个parent_idx的左右两个子节点的大小关系是什么？会对代码的哪些流程产生影响？

    # TODO： 堆里面大家经常说的heapify过程是指什么？和swim什么关系？和sink什么关系？

    def siftup(self, pos):
        endpos = len(self.nums)
        starpos = pos
        newitem = self.nums[pos]

        childpos = 2 * pos + 1  # 左孩子
        while childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and not self.nums[childpos] < self.nums[rightpos]:
                # 左边的要小一点。
                childpos = rightpos
            self.nums[pos] = self.nums[childpos]
            pos = childpos
            childpos = 2 * pos + 1

        pass

    def push(self, num):
        self.nums.append(num)
        self.siftdown()
        # 二叉树形式时，堆顶的数字并非最大或者最小，而是靠近中间的值

        pass

    def pop(self):
        # 删除最左边的， 列表的删除最左边的时间复杂度是多少？
        self.nums[0], self.nums[-1] = self.nums[-1], self.nums[0]
        ans = self.nums.pop()
        self.siftup(0)
        return ans

        # 删除之后在进行heapify

        pass


class MedianFinderMyMethod:
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


class MedianFinderMyHeap:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 为什么普通的不行？
        # 每次都进行一次排序的话一次排序的时间是nO(logn)，n个就是n**2O(logn),时间复杂度太长
        # 两堆就行。

        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass


class MedianFinderHeap:
    def __init__(self):
        self.que_min = []
        self.que_max = []

    def addNum(self, num):
        if not self.que_min or num <= -self.que_min[0]:
            # heapq默认是最小堆，idx=0的时候最小。
            # 但是self.que_min每次要用最大的来比，所以加负号
            # 新进来的数字比最小堆里最大的小，那就应该放在最小堆里。
            heapq.heappush(self.que_min, -num)
            if len(self.que_max) + 1 < len(self.que_min):
                # 总是要保证self.que_max的长度等于self.que_min或者比self.que_min少1，不能少更多
                heapq.heappush(self.que_max, -heapq.heappop(self.que_min))
                pass
        else:
            # 非空，而且新数比最小堆的所有都大
            heapq.heappush(self.que_max, num)
            if len(self.que_max) > len(self.que_min):
                # 总是要保证self.que_min 的长度 >= self.que_max 的。就算大，也只能大1.
                heapq.heappush(self.que_min, -heapq.heappop(self.que_max))

            pass

        pass

    def findMedian(self):
        if (len(self.que_min) > len(self.que_max)):
            return -self.que_min[0]
        return (-self.que_min[0] + self.que_max[0]) / 2

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
            sl = MedianFinderHeap()
            sl = MedianFinderMyMethod()
            sl = MedianFinderMyHeap()
        elif op == "addNum":
            sl.addNum(nums[idx][0])
        elif op == "findMedian":
            print(sl.findMedian())

    pass


if __name__ == "__main__":
    main()
    # nums = [2, 3, 1, 4, 1]
    # heapq.heapify(nums)
    # heapq.heappush(nums, 9)
    # print(nums)
    # print(heapq.heappop(nums))
