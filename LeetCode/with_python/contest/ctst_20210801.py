# -*- coding: utf-8 -*-
"""
@author: Me
@time: 2021/8/1 10:47
@description:
"""

from typing import List


class Solution:
    def numberOfWeeks_dp(self, milestones: List[int]) -> int:
        # 选这个最大可能有多少周？
        # 累加，最后等于milestone?
        n = len(milestones)
        n_week_max = sum(milestones)
        dp = [[0] * (n + 1) for _ in range(n_week_max)]

        for week_idx in range(n_week_max):
            for task_idx in range(n):
                if week_idx == 0:
                    dp[week_idx][task_idx] = 1
                    continue

        pass

    def numberOfWeeks(self, milestones: List[int]) -> int:
        # 动态规划，动态规划的矩阵表格怎么画？
        n_task = len(milestones)

        def helper(last_task_idx, week_idx):
            """
            :param last_task_idx:
            :param week_idx:
            :return:  周数
            """
            cur_num = []
            for idx in range(n_task):
                if idx == last_task_idx:
                    continue
                milestones[idx] -= 1 # 又不能真减？
                cur_num.append(helper(idx, week_idx + 1))

            ans = max(cur_num)

            return ans
                # TODO：所有的选择，不是两个中的选择，怎么做？
            pass
        return helper(-1, 0)

    def minimumPerimeter(self, neededApples: int) -> int:
        l_edge = 0
        n_apple = 0
        while n_apple < neededApples:
            l_edge += 2
            n_idx = l_edge // 2
            new_quater = n_idx * (l_edge + 1) + n_idx*(n_idx+1) - 2*n_idx
            n_apple += 4*new_quater
        return 4*l_edge



def main():

    sl = Solution()

    # milestones = [1, 2, 3]
    # print(sl.numberOfWeeks(milestones))

    needApple = 100000000000000 # 233920
    # needApple = 13 # 8
    # needApple = 1000000000
    print(sl.minimumPerimeter(needApple))

    pass


if __name__ == "__main__":
    main()
