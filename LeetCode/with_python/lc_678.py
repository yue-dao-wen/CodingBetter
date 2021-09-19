# -*- coding: utf-8 -*-
"""
@author: Me
@time: 2021/9/12 20:53
@description:
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        min_cnt, max_cnt = 0, 0  # 先开始的时候，条件卡的很严，最大最小值一样的，也就是说，这样才行。
        for i, c in enumerate(s):
            if c == "(":
                min_cnt += 1
                max_cnt += 1
            elif c == ")":
                min_cnt = max(min_cnt - 1, 0)  # 最少就是不要，不能倒贴吧
                max_cnt -= 1
                if max_cnt < 0:  # 最大值都是负的话，所有的可能都必须是负，还欠你的，凭什么?
                    return False
            elif c == "*":
                min_cnt = max(min_cnt - 1, 0)  # 如果*好看成是)的话，就允许少一个
                max_cnt += 1  # 但是如果看成(了的话，就倒霉多加一个喽~

        return min_cnt == 0
        pass

    def checkValidString_stack(self, s: str) -> bool:
        left_stack = []
        star_stack = []

        for i, c in enumerate(s):
            if c == '(':
                left_stack.append(i)
            elif c == "*":
                star_stack.append(i)
            elif c == ")":
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        while left_stack and star_stack:
            left_idx = left_stack.pop()
            star_idx = star_stack.pop()
            if left_idx > star_idx:
                return False

        return not left_stack

        pass

    def checkValidString_old(self, s: str) -> bool:

        n = len(s)
        memo = {}

        def helper(idx, n_left, n_right):
            # 应该返回个数
            if idx >= n:
                return True
            if (idx, n_left, n_right) in memo:
                return memo[(idx, n_left, n_right)]

            c = s[idx]
            res_tmp = False
            if c == '(':
                n_left += 1
                res_tmp = helper(idx + 1, n_left, n_right)
            elif c == ")":
                n_right += 1
                res_tmp = helper(idx + 1, n_left, n_right)
            elif s[idx] == '*':
                con1 = helper(idx + 1, n_left + 1, n_right)
                con2 = helper(idx + 1, n_left, n_right + 1)
                con3 = helper(idx + 1, n_left, n_right)
                res_tmp = con1 or con2 or con3
            pass

            res = res_tmp

            memo[(idx, n_left, n_right)] = res
            return res

        return helper(0, 0, 0)


def main():
    sl = Solution()

    test_case = {
        # 字符串为空
        '': True,
        # 只有一个字符
        "(": False,
        ")": False,
        "*": True,
        # 有俩字符串的：
        '()': True,
        '(*': True,
        '((': False,
        '*)': True,
        '*(': False,
        "**": True,
        ")(": False,
        ")*": False,
        "))": False,
        # 有3的：
        "((*)": True,
        "(*)": True,
        "(*))": True,

    }

    for s, gt in test_case.items():
        res = sl.checkValidString(s)
        if res != gt:
            print(f"{s}: don't pass")
        # print(f"{s}: pass." if res == gt else f"{s}: don't pass")
    pass


if __name__ == "__main__":
    main()
