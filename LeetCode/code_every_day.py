from collections import deque
from typing import Counter, List
from functools import lru_cache
from collections import defaultdict
import math
import re

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
        self.is_end = False # 标记是否是一个单词的结尾
        self.val = 0    # 当前节点的值
        self.ssum = 0    # 以当前为前缀的所有词的值的和
        pass
    
    def insert(self, word, val=0, delta=0):
        node = self # node可以是自己，这种用法很酷啊
        for c in word:
            c_idx = ord(c) - ord("a")
            if not node.children[c_idx]:
                node.children[c_idx] = TrieNode()
            node = node.children[c_idx]
            node.ssum += delta # ssum值跟前缀中每个单词都有关系
        node.is_end = True
        node.val = val # val值只需要在单词最后一个位置加就行
    
    def find_last_node(self, prefix):
        node = self
        for c in prefix:
            c_idx = ord(c) - ord('a')
            if node.children[c_idx] is None:
                return None
            node = node.children[c_idx]
        return node

    def is_words(self, word, start):
        if start == len(word):
            return True
        node = self
        for i in range(start, len(word)):
            node = node.children[ord(word[i]) - ord('a')]
            if node is None:
                return False
            if node.is_end and self.is_words(word, i+1):
                return True
        return False

   

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



class MapSum_PrefixMap:

    def __init__(self):
        self.word_map = defaultdict(int)
        self.prefix_map = defaultdict(int)

    def insert(self, word: str, wval: int) -> None: # 将函数签名改为word和wval, 可读性更强。
        delta = wval
        # 对于为什么要设置一个delta，思考这样一个问题。如果insert函数先后输入两组值：("leetcode", 10)和("leetcode", 20)。
        # "leetcode"这个词的两个wval，是两个都算还是只算一个？如果只算一个，应该算哪个呢？
        # 因为是同一个词，当然只算一个。因为涉及到更新，所以当然要算第二个。
        # 之所以要设计一个delta, 就是出于这个原因，解决word相同，而wval不同的情况。
        # 这种情况下，key没有变，不能当做新来一个词那样，给所有的prefix添加新的wval，而是需要更新。
        # delta就是就算的新wval 和旧的wval之间的差值，用这个差值去给所有涉及到的prefix赋值就行了。 
        if word in self.word_map:   # 如果已经见过这个单词, 就不应该继续赋值，而是刷新。
            delta -= self.word_map[word]
        self.word_map[word] = wval
        for i in range(len(word)):
            prefix = word[:i+1]  # 每种前缀都会出现
            self.prefix_map[prefix] += delta
           
    def sum(self, prefix: str) -> int:
        return self.prefix_map.get(prefix, 0)


class MapSum_Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        self.word_map = {}

    def insert(self, word, wval):
        delta = wval
        if word in self.word_map:
            delta -= self.word_map[word]
        self.word_map[word] = wval

        self.root.insert(word, delta=delta)
    
    def sum(self, prefix):
        node = self.root.find_last_node(prefix)
        return node.ssum if node else 0


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        # 预计算
        tops = []
        top_count = defaultdict(int)
        top_count[-1] = -1 # 为啥是-1？不是0？
        cur_top = -1
        for p in persons:
            top_count[p] += 1
            if top_count[p] > top_count[cur_top]:
                cur_top = p
            tops.append[p]
        self.tops = tops
        self.times = times
        pass

    def q(self, t: int) -> int:
        l, r = 0, len(self.times) - 1
        while l < r:
            m = l + (r -l + 1) // 2
            if self.times[m] <= t:
                l = m
            else:
                r = m -1
        return self.tops[l]
        
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
    
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # 解法1：最小堆。
        # 为什么要用最小堆呢？
        ans = 0
        n_row = len(heightMap)
        n_col = len(heightMap)
        water_height = [[0] * n_col for _ in range(n_row) ]
        for i in range(n_row):
            for j in range(n_col):
                if i == 0 or j == 0 or i == n_row - 1 or j == n_col - 1:
                    water_height[i][j] = heightMap[i][j]
                else:
                    # 左上角肯定是已经有了的
                    water_height[i][j] = 0
        
        # 左上角肯定是已经有了的。
        
        pass
    
    def bulbSwitch(self, n: int) -> int:
        # bulb_id: 会被切换的轮次代号
        # 1: 1、
        # 2: 1、 2、
        # 3: 1、    3、
        # 4: 1、 2、    4、
        # 5: 1、            5、
        # 6: 1、 2、3、         6、
        # 7: 1、                    7、
        # 8: 1、 2、    4、             8、
        # 9: 1、    3、                     9、
        # 10: 1、 2、       5、                 10、
        # 找规律：
        # (1) 第 k 个灯泡会在其所有约数的轮次中被拨开关。
        # (2) 因为最开始的时候都是灭的，动单数词，亮；动双数次，灭。要找多少个亮，就找有单数个约数的编号。
        # (3) 观察上面发现有单数个约束的是：1/4/9。完全平方数！因为完全平方数有两个约束相等！
        # (4) 某个范围n内，完全平方数的个数：开方向下取整=x。x^2肯定小于n，在范围n内。(x-1)^2也肯定在这个范围内。
        # (5) 为了避免精度问题，加一点小数。
        return int(math.sqrt(n + 0.5))

        pass

    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # 各自面积加起来=最左上角最右下角的面积
        # 重复的刚好是空缺的，就不行, 顶点次数。
        x_min, y_min, x_max, y_max = float("inf"), float("inf"), float('-inf'), float('-inf')
        sum_area = 0
        for (x_left, y_down, x_right, y_up) in rectangles:  # right >= left, up >= down
            cur_area = (x_right - x_left) * (y_up - y_down)
            sum_area += cur_area
            x_min = min(x_min, x_left)
            x_max = max(x_max, x_right)
            y_min = min(y_min, y_down)
            y_max = max(y_max, y_up)
        
        mmax_area = (x_max -x_min) * (y_max - y_min)

        return sum_area == mmax_area

    def integerReplacement(self, n: int) -> int:
        # 加的话，会变大。上限怎么办？
        memo = {}
        def helper(num):
            if num == 1:
                return 0
            if num in memo:
                return memo[num]
            res = float("inf")
            if num % 2 == 0:
                res = helper(num // 2) + 1
            else:
                left = helper(num -1) + 1
                right = helper(num + 1) + 1
                res =  min(left, right)
            memo[num] = res
            return res

        return helper(n)

    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        min_frac, max_frac = 0.0, 1.0 

        while True:
            cur_frac = (min_frac + max_frac) / 2
            numerator_idx = -1
            cnt_smaller_than_mid = 0
            ans_numerator, ans_denominator = 0, 1 # 最大的分数是1， 最小的分数是0。

            for denominator_idx in range(1, n):
                while arr[numerator_idx + 1] / arr[denominator_idx] < cur_frac:
                    numerator_idx += 1
                    # 相当于比较两个分数的大小：a/b > c/d <=> a * d > c * b
                    if arr[numerator_idx] * ans_denominator > arr[denominator_idx] * ans_numerator: 
                        ans_numerator, ans_denominator = arr[numerator_idx], arr[denominator_idx]
                cnt_smaller_than_mid += numerator_idx +  1

            if cnt_smaller_than_mid == k:
                return [ans_numerator, ans_denominator]

            if cnt_smaller_than_mid < k:
                min_frac = cur_frac
            else:
                max_frac = cur_frac

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        desc = ["Gold Medal", "Silver Medal", "Bronze Medal" ]
        arr = sorted(enumerate(score), key=lambda x:-x[1])
        ans = [""] * len(score)
        for i, (idx, _) in enumerate(arr):  # 记录两个顺序。
            ans[idx] = desc[i] if i < 3 else str(i + 1)
        return ans

            
            

            

        pass

    def validTicTacToe(self, board: List[str]) -> bool:
        # X - O = 1 / 0
       
        cnt_x = 0
        cnt_o = 0
        
        for string in board:
            for c in string:
                cnt_x += 1 if c == 'X' else 0
                cnt_o += 1 if c == 'O' else 0
        
        if not (cnt_x == cnt_o or cnt_x - cnt_o == 1):
            return False

        is_v1_same = board[0][0] == board[1][0] == board[2][0]
        is_v2_same = board[0][1] == board[1][1] == board[2][1]
        is_v3_same = board[0][2] == board[1][2] == board[2][2]
        is_lefttop_same = board[0][0] == board[1][1] == board[2][2]
        is_righttop_same = board[0][2] == board[1][1] == board[2][0]
        is_h1_same = board[0] == 'XXX' or board[0] == 'OOO'
        is_h2_same = board[1] == 'XXX' or board[1] == 'OOO'
        is_h3_same = board[2] == 'XXX' or board[2] == 'OOO'


        is_x_win = (board[0][0] == 'X' and (is_v1_same or is_h1_same or is_lefttop_same)) or ()

        return (is_v1_same + is_v2_same + is_v3_same + is_lefttop_same + is_righttop_same + is_h1_same + is_h2_same + is_h3_same) <=1

    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        n_person = len(quiet)
        graph = [[] for _ in range(n_person)]
        for r in richer:
            graph[r[1]].append(r[0])
        
        ans = [-1] * n_person
        def dfs(x):
            if ans[x] != -1:
                return # 已经找到了
            ans[x] = x  # 没有比自己更有钱的人时，最安静的是自己
            for y in graph[x]: # 遍历所有比自己有钱或者比自己更有钱的人，找出最安静的那个
                dfs(y)
                if quiet[ans[y]] < quiet[ans[x]]:
                    ans[x] = ans[y]
        
        for i in range(n_person):
            dfs(i) # 对每个人都找“和他一样有钱，或者比他更有钱的”人当中，最安静的那个
        
        return ans




        

        
        
        
        pass
    
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        # 解法2：正则表达式
        return re.findall(fr'\b{first} (?={second} ([\w]+))\b', text)
        return re.findall(fr"(?<=\b{first} {second} )(\w+)", text)
        # 解法1：双指针
        # if not text:
        #     return []
        # text = text.split(' ')
        # len_text = len(text)
        # if len_text < 3:
        #     return []
        # ans = []
        # left, right = 0, 1
        # while right < len_text:
        #     while right < len_text and (text[left] != first or text[right] != second):
        #         left += 1
        #         right += 1
        #     if right + 1 < len_text:
        #         ans.append(text[right + 1])
        #     else:
        #         break
        #     left += 1
        #     right += 1
        
        # return ans
    def numFriendRequests(self, ages: List[int]) -> int:
        # 解法2：前缀和
        # 新增刷题经验：
        # 1. 简化条件，找到考虑单调递增和递减的边界。
        # 2. 遇到一个数组中所有数组两两比较/组合的情况，可以考虑使用计数排序 + 前缀和
        # 3. 函数化：年龄变了，条件就变了，针对不同的年龄，思考各自的条件。
        cnt = [0] * 121
        for age in ages: # 这组年龄里面，有些数字会出现多次，放在一个计数数组里，可以只算一次。
            cnt[age] += 1
        # 对于年龄age来说，有符合条件的边界。(0.5 * age + 8, age]。如果这个范围是整个age，那就直接求和就行；
        # 现在只是某个范围的一部分，那就减去不符合的部分就行了。pre_sum其实就是从最左到某一个点的求和。
        # e.g: (2, 5] = [1, 10] - [1, 2] - (5, 10]
        # 这样的话，就算不是单调的，有多个可能的条件，也可以用这种区间相减的方式得到。
        pre_sum = [0] * 121     # 可以从数列和的角度来理解前缀和。
        for i in range(1, 121):
            pre_sum[i] = pre_sum[i-1] + cnt[i]
        
        ans = 0
        for i in range(15, 121):
            if cnt[i] > 0:
                bound = int(i * 0.5 + 8)
                ans += cnt[i] * (pre_sum[i] - pre_sum[bound - 1] - 1) # -1 是减去自己，可以和同岁的发消息，所以只需要-1，而不需要把所有同龄都减掉。
        return ans

        # # 解法1：双指针
        # l = len(ages)
        # ages.sort()
        # left = right = ans = 0
        # for age in ages:
        #     if age < 15:
        #         continue
        #     while ages[left] <= 0.5 * age + 7:
        #         left += 1
        #     while right + 1 < l and ages[right + 1] <= age:
        #         right += 1
        #     ans += right - left
        
        # return ans
    
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # 刷题经验：
        # 1. 由短字符串组成长字符串，先排序，以免还要想办法做动态规划，找最长的。e.g.: catsdog = [0, 0, 1, 1, 0, 0, 1]需要判断要不要从第一个1停止。
        #    从短到长添加时，'dogcatsdog' 到t时，is_end，但是剩余的不是。没关系，可以走下一个字母，所以就挽救回来了。
        words.sort(key=len)
        # print(words)
        ans = []
        trie = TrieNode()
        for word in words:
            if word == "":
                continue
            if trie.is_words(word, 0):
                ans.append(word)
            else:
                trie.insert(word)
        # print(ans)
        return ans

def run_lc472():
    sl = Solution()
    words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    sl.findAllConcatenatedWordsInADict(words)
    pass


def run_lc825():
    pass


def run_lc1078():
    sl = Solution()
    text =  "alice is aa good girl she is a good student"
    first = "a"
    second = "good"
    print(sl.findOcurrences(text, first, second))
    pass

def run_lc851():
    pass

def run_lc794():
    sl = Solution()

    board = ["O  ","   ","   "]
    # board = ["XOX"," X ","   "]
    # board = ["XXX","   ","OOO"]
    # board = ["XOX","O O","XOX"]
    board = ["XXX","OOX","OOX"]
    print(sl.validTicTacToe(board))
    pass


def run_lc786():
    pass


def run_lc397():
    sl = Solution()
    n = 8
    n = 7
    n = 4
    n = 1
    n = 2**31 -1
    n = 100
    print(sl.integerReplacement(n))
    pass
            



def run_lc391():
    sl = Solution()
    rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
    # rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
    # rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[3,2,4,4]]
    # rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
    # rectangles = [[0,0,1,1],[0,1,3,2],[1,0,2,2]]
    print(sl.isRectangleCover(rectangles))
    pass



def run_lc319():
    sl = Solution()
    print(sl.bulbSwitch(10))

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
    # run_lc240()
    # run_lc319()
    # run_lc391()
    # run_lc397()
    # run_lc794()
    # run_lc1078()
    run_lc472()

    pass


if __name__ == "__main__":
    main()