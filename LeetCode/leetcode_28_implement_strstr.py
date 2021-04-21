class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 解法2：
        if needle == "":
            return 0
        l_h, l_n = len(haystack), len(needle)
        if l_h < l_n:
            return -1
        for start in range(l_h):
            if haystack[start:start+l_n] == needle:
                return start
        return -1


        # # 解法1：时间复杂度是nm，过不了。
        # if needle == '':
        #     return 0
        # l_hay, l_need = len(haystack), len(needle)
        # if l_need > l_hay:
        #     return -1
        #
        # def start_with(idx):
        #     i, j = 0, idx
        #     while i < l_need and j < l_hay:
        #         if haystack[j] != needle[i]:
        #             return False
        #         j += 1
        #         i += 1
        #     return i == l_need
        #
        # i_h = 0
        # while i_h < l_hay:
        #     if haystack[i_h] == needle[0] and start_with(i_h):
        #         return i_h
        #     i_h += 1
        return -1


if __name__ == '__main__':
    sl = Solution()
    h = "abdabd"
    n = 'bda'
    n = "abc"
    haystack = "hello"
    needle = "ll"
    haystack = "aaaaa"
    needle = "bba"
    haystack = ""
    needle = ""
    haystack = "aaa"
    needle = "aaaa"
    haystack = "mississippi"
    needle = "issipi"
    print(sl.strStr(haystack, needle))
