from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l_nums = len(nums)
        res_len = len(nums)
        last_idx = 0
        idx = 0
        while idx < l_nums:
            if nums[idx] == val:
                idx += 1
                res_len -= 1
                continue
            nums[last_idx] = nums[idx]
            last_idx += 1
            idx += 1

        while len(nums) != last_idx:
            nums.pop()
        # print(nums)
        return res_len


if __name__ == '__main__':
    sl = Solution()
    # nums = [1, 2, 3]
    nums = [3, 2, 2, 3]
    val = 3
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(sl.removeElement(nums, val))
