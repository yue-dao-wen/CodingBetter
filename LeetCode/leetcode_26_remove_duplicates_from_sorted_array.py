from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        l_nums = len(nums)
        if l_nums == 1:
            return l_nums
        pre_num = nums[0]
        last_idx = 1
        res_len = 1
        idx = 1
        while idx < l_nums:
            if nums[idx] == pre_num:
                idx += 1
                continue
            res_len += 1
            nums[last_idx] = nums[idx]
            pre_num = nums[idx]
            last_idx += 1
            idx += 1
        # python list 不同操作的复杂度不同， remove的复杂度太大，用pop:https://blog.csdn.net/qq_45949008/article/details/103375664
        while len(nums) != last_idx:
            nums.pop()
        print(nums)
        return res_len


if __name__ == '__main__':
    sl = Solution()
    # nums = [1, 2, 3]
    nums = [1, 1, 2]
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(sl.removeDuplicates(nums))
