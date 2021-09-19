# -*- coding: utf-8 -*-
"""
@author: Me
@time: 2021/9/14 22:47
@description:
"""

from typing import List


def is_attainable(tar, string):
    t, s = 0, 0
    l_tar = len(tar)
    l_str = len(string)
    while t < l_tar and s < l_str:
        if tar[t] == string[s]:
            t += 1
            s += 1
        else:
            s += 1

    return t == l_tar


class Solution:

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res = ""
        dictionary.sort(key=lambda x: [-len(x), x])
        for idx, tar in enumerate(dictionary):
            if is_attainable(tar, s):
                res = tar
                break
        return res

        pass


def main():
    sl = Solution()

    s = "abpcplea"
    dictionary = ["ale", "apple", "monkey", "plea"]

    s = "abpcplea"
    dictionary = ["a", "b", "c"]

    s = "abce"
    dictionary = ["abe", "abc"]

    print(sl.findLongestWord(s, dictionary))
    pass


if __name__ == "__main__":
    main()
