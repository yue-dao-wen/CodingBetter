### 一、解题思路
**1. 整体思路很简单：**

一般来说,对于每个房子有抢或者不抢两种选择，哪种选择能够实现利益最大化，就选哪种。这其实就是个`max(yes, no))`过程。`yes`代表抢后得到的钱，`no`是不抢的钱。

这道题比较特殊的一点是第一个房子抢劫与否会影响到最后一个房子，用最简单的思路把这个事情考虑进去就是：用一个变量记住第一个房子的选择，到最后一个房子的时候参考这个选择做出决定就行了。

**2. 细节实现：**

对于某个房子，需要算出对他进行选择之后得到的钱，所以需要一个函数计算得到`yes`和`no`的值。这个函数除了和`到底是哪个房子`、`到这个房子的时候已经有多少钱了`有关之外，还需要记住`第一个房子有没有被抢`，因为第一个房子有没有被抢会一直影响到最后。

所以整个函数的入口应该是`helper(idx, money, rob_first=False)`.

**3. 一些优化：**


一组具体的`(idx, money, rob_first=False)`值是一个状态，这个状态在递归过程中可能会重复出现，为了避免重复运算，就直接放入一个memo中。


### 二、代码

```python3
class Solution:
    def rob(self, nums: List[int]) -> int:
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
```