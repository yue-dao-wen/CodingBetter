class Solution:
    def numDecodings(self, s: str) -> int:
        # 解法1： 回溯算法？
        if s == "0":
            return 0
        l_s = len(s)
        ans = []
        def help(idx):
            if idx >= l_s:
                return
            pass


            if idx == l_s - 2 and s[-1] == '0':
                one, two = 0, 1
                return one + two

            # 要么用1个字母
            one = help(idx+1)

            # 要么用2个字母
            two = help(idx + 2)
            return one + two






        pass
