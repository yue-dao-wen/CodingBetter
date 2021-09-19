# -*- coding: utf-8 -*-
"""
@author: Me
@time: 2021/9/19 15:45
@description:
"""


class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0] * (n + 1)
        # dp[l]表示要得到长度为l的字符串，需要的操作次数
        for l in range(2, n + 1):
            dp[l] = float("inf")  # 因为求最少，将初始值设置为无穷大，即得到长度为l的字符串需要无穷长的操作次数。
            l_clp_brd = 1  # 已经在粘贴板里的字符串的长度

            # 1、最初思路：
            # while l_clp_brd < l:  # 不能傻到已经复制长度到了，还要复制吧。所以粘贴板里字符串的长度肯定比目的字符串的长度短
            #     if l % l_clp_brd == 0:  # 如果期望的长度刚好是粘贴板字符串长度的整数倍，就可以直接复制粘贴啦
            #         dp[l] = min(dp[l], dp[l_clp_brd] + l // l_clp_brd - 1 + 1)  # ：
            #         # 得到粘贴板里的字符串也需要一些操作，所以要把dp[l_clp_brd]加上；
            #         # “- 1”表示“有一个已经在啦，所以可以少粘贴一次”；
            #         # “+1”表示“别忘了还复制了一次嗷”， 然后一正一负就没了
            #     l_clp_brd += 1  # 能不能被整除都可以尝试粘贴板里长度+1之后会怎么样
            #
            # # 2、第一次优化：
            # while l_clp_brd < l:
            #     if l % l_clp_brd == 0:
            #         dp[l] = min(dp[l], dp[l_clp_brd] + l // l_clp_brd)
            #         dp[l] = min(dp[l], dp[l // l_clp_brd] + l_clp_brd)  # ：
            #         # 长度为3的粘贴2此可以，那长度2的粘贴3次也可以喽~偷个懒
            #     l_clp_brd += 1

            # 3、第三次优化
            while l_clp_brd * l_clp_brd <= l:  # ：
                # 填充l_clp_brd的时候已经把l // l_clp_brd也填充了，所以到了 l 开方之后的就没必要再做一次循环啦
                if l % l_clp_brd == 0:
                    dp[l] = min(dp[l], dp[l_clp_brd] + l // l_clp_brd)
                    dp[l] = min(dp[l], dp[l // l_clp_brd] + l_clp_brd)
                l_clp_brd += 1

        return dp[n]

    def minSteps_recursion(self, n: int) -> int:
        if n == 1:
            return 0

        memo = {}

        def helper(l_s, cnt_op, is_cp):
            if l_s == n:
                return cnt_op
            if (l_s, cnt_op) in memo:
                return memo[(l_s, cnt_op)]

            if is_cp:
                res = helper(l_s, cnt_op + 1, False)  # 下一次就不要在copy啦
            else:
                res = helper(l_s * 2, cnt_op + 1, True)

            memo[(l_s, cnt_op)] = res
            return res

        return helper(1, 1, 1)

        # # 大家都是怎么命名的？
        # # 不需要动态规划，判断就行。
        # # 最少需要多少次操作？
        #
        # dp = [float('inf')] * n
        # # dp[i] 表示要得到长度为i的字符串，所需要的最少的操作次数。
        # dp[0] = -1  # 通常设置数组为多长？开头和结尾的数值应该怎么确定？
        # dp[1] = 0
        # dp[2] = 2  # 复制一次，粘贴一次
        # dp[3] = 3  # 复制1次，粘贴2次
        #
        # pass


def main():
    sl = Solution()
    # print(sl.minSteps(4))

    for n in range(3, 9):
        res = sl.minSteps(n)
        print(res)
        # print(sl.minSteps(n))

    pass


if __name__ == "__main__":
    main()
