class Solution:
    def numDecodings(self, s: str) -> int:
        # 解法2：

        if s == "":
            return 0
        l_s = len(s)
        if l_s == 1:
            return 1
        i = 0
        pre_pre, pre = 0, 1
        while i < l_s:

            if s[i - 1] != '0':
                tmp += pre
            if s[i - 2] != '0' and int(s[i - 2:i]) <= 26:
                tmp += pre_pre
            pre_pre, pre, tmp = pre, tmp, 0
            i += 1

        return pre

        # 解法1:
        # if s == "":
        #     return 0
        # l_s = len(s)
        # if l_s == 1:
        #     return 1
        # dp = [1] + [0] * l_s
        # for i in range(1, l_s + 1):
        #     # 往前一个行不行？增加1个行不行？
        #     if s[i - 1] != "0":
        #         dp[i] += dp[i - 1]
        #     # 往前两个行不行？增加2个行不行？
        #     if i > 1 and s[i - 2] != "0" and int(s[i - 2:i]) <= 26:
        #         dp[i] += dp[i - 2]
        # return dp[l_s]


def main():
    sl = Solution()
    num = "123"
    num = "0"
    num = "1"
    num = "123456"
    num ="226"
    print(sl.numDecodings(num))
    pass


if __name__ == '__main__':
    main()
