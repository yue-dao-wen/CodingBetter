from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # 动态规划？
        # 1. 记住第一个？
        l_nums = len(nums)
        memo = {}

        def helper(idx, money, rob_first=False):
            if (idx, money, rob_first) in memo:
                return memo[(idx, money, rob_first)]

            if idx == 0:
                yes = helper(idx + 2, money + nums[idx], True)
                no = helper(idx + 1, money, False)
                res = max(yes, no)
            elif idx == l_nums - 1:
                res = money if rob_first else money + nums[idx]
                pass
            elif idx > l_nums - 1:
                res = money
                pass
            else:
                yes = helper(idx + 2, money + nums[idx], rob_first)
                no = helper(idx + 1, money, rob_first)
                res = max(yes, no)

            memo[(idx, money, rob_first)] = res
            return res

        return helper(0, 0, False)


if __name__ == '__main__':
    sl = Solution()

    # nums = [1, 2, 3, 1]
    nums = [2, 3, 3]
    # nums = [0]
    nums = [4, 1, 2, 7, 5, 3, 1]
    print(sl.rob(nums))
