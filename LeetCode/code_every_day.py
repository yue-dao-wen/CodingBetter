
from collections import deque
from typing import List
from functools import lru_cache

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_link_list(head):
    nums = []
    while(head):
        nums.append(head.val)
        head = head.next
    print(nums)



def build_link_list(nums):

    pass



def build_multi_level_doubly_link_list(nums):
    # 遇到第二个None就是第二层了。
    # 相比于上一个空几个None
    if not nums:
        return None
    # 建立主链
    p_dump = Node(-1, None, None, None)
    pre = p_dump
    i = 0
    n = len(nums)
    while(i < n and nums[i] != None):
        new_node = Node(nums[i], None, None, None)
        pre.next = new_node
        new_node.prev = pre
        pre = new_node
        i += 1
    
    # 找到是哪个节点需要孩子
    need_child = p_dump.next
    i += 1
    while(i < n and nums[i] == None):
        need_child = need_child.next
        i += 1
        pass
    child = None if i >= n else build_multi_level_doubly_link_list(nums[i:])
    need_child.child = child
    return p_dump.next


def get_nums_of_multi_level_doubly_link_list(head):
    cur = head
    next_level_head = None
    nums = []
    while(cur):
        nums.append(cur.val)
        if cur.child:
            next_level_idx = len(nums) - 1
            next_level_head = cur.child
        cur = cur.next
    # nums.append("\n")
    
    if next_level_head != None:
        idx = 0
        while idx != next_level_idx:
            nums.append("#")
            idx += 1
        nums += get_nums_of_multi_level_doubly_link_list(next_level_head)
    
    return nums
  


def print_nums(nums):
    if not nums:
        print("空")
        return
    string = ", ".join(str(n) for n in nums)
    print(string)
    pass

class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.is_end = False
        pass
    
    def insert(self, word):
        node = self # node是自己就很酷
        for c in word:
            c_idx = ord(c) - ord("a")
            if not node.children[c_idx]:
                node.children[c_idx] = TrieNode()
            node = node.children[c_idx]
        node.is_end = True
   

class WordDictionary:

    def __init__(self):
        self.tire = TrieNode()
        pass


    def addWord(self, word: str) -> None:
        self.tire.insert(word)
        pass

    def search(self, word: str) -> bool:
        def dfs(idx, node):
            if idx == len(word):
                return node.is_end
            
            c = word[idx]
            if c != ".":
                child = node.children[ord(c) - ord('a')]
                if child and dfs(idx + 1, child):
                    return True
                # return child and dfs(idx + 1, child)
            else:
                for child in node.children:
                    if child is not None and dfs(idx + 1, child):
                        return True
            return False

        return dfs(0, self.tire)

def run_lc211():
    ops = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    ipts = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    wd = None
    for op, ipt in zip(ops, ipts):
        if op == "WordDictionary":
            wd = WordDictionary()
        elif op == "addWord":
            wd.addWord(ipt[0])
        elif op == "search":
            print(wd.search(ipt[0]))





class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def dfs(node):
            cur = node
            last = None
            while cur:
                nxt = cur.next
                if cur.child is None:
                    # 如果没有孩子
                    last = cur
                else:
                    #  如果有孩子, next 要变成孩子, 孩子的last要变成cur
                    # 孩子还有孩子，要先把孩子的一连串遍历完了在结自己的，所以要知道孩子的最后一个last是谁
                    
                    # 找到孩子那一辈的最后一个
                    child_last = dfs(cur.child)

                    # 自己和孩子的头连起来
                    cur.next = cur.child
                    cur.child.prev = cur
                    cur.child = None 

                    # 孩子的尾巴和自己的下一个连起来
                    child_last.next = nxt
                    if nxt:
                        nxt.prev = child_last

                    last = child_last

                cur = nxt
            return last
           

        dfs(head)
        return head

    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        l = dp[l1][l2]
        return l1 - l + l2 - l
    def getSum(self, a: int, b: int) -> int:

        N_DIGIT = 32
        MASK_NUM_CNT = 2 ** N_DIGIT # 可以表示的数字的个数。
        MAST_POS_CNT = 2 ** (N_DIGIT - 1) # 负数的0，可以表示的数里面，最高位是1，其余都是0
        MASK_MAX_POS = MAST_POS_CNT - 1
        

        a %= MASK_NUM_CNT # 如果溢出了
        b %= MASK_NUM_CNT # 如果溢出了

        while b != 0:   # b为什么终究会变成0？b=c，c一直左移。左移是为了进位。
            c = ((a & b) << 1) % MASK_NUM_CNT
            s = (a ^ b) % MASK_NUM_CNT

            b = c
            a = s
        
        if a & MAST_POS_CNT:
            a = a^ MAST_POS_CNT
            a = a ^ MASK_MAX_POS
            a = ~a  # 0 取反是-1
        
        return a



    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # todo: 这个题还有别的解法，至少3种
        def dfs_sum(node, target):
            if node is None:
                return 0
            
            res = 0
            if node.val == target:
                res += 1
            
            res += dfs_sum(node.left, target - node.val)
            res += dfs_sum(node.right, target - node.val)

            return res

        if root is None:
            return 0
        
        res = dfs_sum(root, targetSum)
        res += self.pathSum(root.left, targetSum)
        res += self.pathSum(root.right, targetSum)
        return res



        
        
        
        pass

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = []
        for c in s:
            if c == "-":
                continue
            if c.isalpha():
                chars.append(c.upper())
            else:
                chars.append(c)
        
        n = len(chars)
        n1 = n % k
        res = "".join(chars[:n1])
        for i in range(n1, n, k):
            cur = "".join(chars[i:i+k])
            if res != "":
                res += "-"
            res += cur
        res.lstrip('-')
        return res

    def countSegments(self, s: str) -> int:
        # res = 0
        # s = s.strip().split(" ")
        # for c in s:
        #     if c != "":
        #         res += 1
        return len([c for c in s.strip().split(" ") if c != ""])
        # return res
    def minMoves(self, nums: List[int]) -> int:
        ans = 0
        mmin = min(nums)
        for n in nums:
            ans += n - mmin
        return ans

    def shoppingOffers_lc(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)

        # 过滤不需要计算的大礼包，只保留需要计算的大礼包
        filter_special = []
        for sp in special:
            if sum(sp[i] for i in range(n)) > 0 and sum(sp[i] * price[i] for i in range(n)) > sp[-1]:
                filter_special.append(sp)

        # 记忆化搜索计算满足购物清单所需花费的最低价格
        @lru_cache(None)
        def dfs(cur_needs):
            # 不购买任何大礼包，原价购买购物清单中的所有物品
            min_price = sum(need * price[i] for i, need in enumerate(cur_needs))
            for cur_special in filter_special:
                special_price = cur_special[-1]
                nxt_needs = []
                for i in range(n):
                    if cur_special[i] > cur_needs[i]:  # 不能购买超出购物清单指定数量的物品
                        break
                    nxt_needs.append(cur_needs[i] - cur_special[i])
                if len(nxt_needs) == n:  # 大礼包可以购买
                    p = dfs(tuple(nxt_needs)) + special_price
                    min_price = min(min_price, p)
            return min_price

        return dfs(tuple(needs))


    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n_kind = len(price)
        
        special_valid = []
        for sp in special:
            ssum = sum(sp[:n_kind])
            if ssum > 0 and sum(sp[i] * price[i] for i in range(n_kind)) > sp[-1]:
                special_valid.append(sp)
                
        @lru_cache(None)
        def dfs(cur_needs):
            min_price = sum(cur_needs[i] * price[i] for i in range(n_kind))
            for sp in special_valid:
                # 先看礼包
                next_needs = []
                for i in range(n_kind):
                    if sp[i] > cur_needs[i]:
                        break
                    next_needs.append(cur_needs[i] - sp[i])
                if len(next_needs) == n_kind:
                    p = dfs(tuple(next_needs)) + sp[-1]
                    min_price = min(min_price, p)
            
            return min_price
        
        res = dfs(tuple(needs))
        return res
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 二分法
        n_row = len(matrix)
        if n_row == 0:
            return False
        n_col = len(matrix[0])
        x, y = 0, n_col - 1
        while x < n_row and y >= 0:
            if matrix[x][y] > target:
                y -= 1
            elif matrix[x][y] < target:
                x += 1
            elif matrix[x][y] == target:
                return True
        
        return False

def run_lc240():
    sl = Solution()
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    target = 100
    target = -1

    print(sl.searchMatrix(matrix, target))


    pass

 

def run_lc638():
    # 测试用例
    sl = Solution()
    price = [2,5]
    special = [[3,0,5],[1,2,10]]
    needs = [3,2]

    price = [2,3,4]
    special = [[1,1,0,4],[2,2,1,9]]
    needs = [1,2,1]

    price = [2,3]
    special = [[1,0,1],[0,1,2]]
    needs = [1,1]

    print(sl.shoppingOffers(price, special, needs))
    
  
    

    pass


def run_lc453():
    sl = Solution()
    
    nums = []
    nums = [1, 1, 1]
    nums = [1, 2]
    nums = [1, 2, 3]
    nums = [3, 2, 1]
    nums = [1, 2, 4]

    print(sl.minMoves(nums))

    pass


        

def run_lc482():
    sl = Solution()
    S = "5F3Z-2e-9-w"
    K = 4

    S = "2-5g-3-J"
    K = 2

    print(sl.licenseKeyFormatting(S, K))

    pass


                
            
            

def run_lc437():
    nums = [10,5,-3,3,2,None,11,3,-2,None,1]


    pass


def run_lc371():
    a = 3
    b = 7

    a = -3
    b = 2
    sl = Solution()
    print(sl.getSum(a, b))
    pass


def run_lc583():
    string1 = "sea"
    string2 = "eat"
    sl = Solution()
    print(sl.minDistance(string1, string2))
    pass



def run_lc430():
    nums = [1,2,3,4,5,6,None,None,None,7,8,9,10,None,None,11,12]
    nums = [1,2,None,3]
    nums = []
    head = build_multi_level_doubly_link_list(nums)
    print_nums(get_nums_of_multi_level_doubly_link_list(head))
    sl = Solution()
    new_head = sl.flatten(head)
    print_nums(get_nums_of_multi_level_doubly_link_list(new_head))

    pass


def main():
    # run_lc430()
    # run_lc583()
    # run_lc371()
    # run_lc482()
    # run_lc453()
    # run_lc211()
    # run_lc638()
    run_lc240()
    pass


if __name__ == "__main__":
    main()