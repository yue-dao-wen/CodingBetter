# -*- coding: utf-8 -*-
"""
@author: Me
@time: 2021/8/14 22:50
@description:
"""

from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:

        def get_prf(a, b):
            for i, x in enumerate(preferences[a]):
                if x == b:
                    return i
            return -1

        pair_dict = {}
        for x, y in pairs:
            pair_dict[x] = y
            pair_dict[y] = x

        happy_set = set()
        unhappy_set = set()
        for x in range(n):
            if x in happy_set or x in unhappy_set:
                continue
            for idx, y in enumerate(preferences[x]):
                # 我与你的关系好过我和我的现任
                # 你和我的关系也好过你和你的现任
                # 我就不开心
                x2y = get_prf(x, y)
                x2xp = get_prf(x, pair_dict[x])

                y2x = get_prf(y, x)
                y2yp = get_prf(y, pair_dict[y])

                if x2xp == 0:
                    happy_set.add(x)
                if y2yp == 0:
                    happy_set.add(y)

                if x2y < x2xp and y2x < y2yp:
                    unhappy_set.add(x)
                    unhappy_set.add(y)

        return len(unhappy_set)


def main():
    sl = Solution()
    n = 4
    preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
    pairs = [[0, 1], [2, 3]]

    n = 2
    preferences = [[1], [0]]
    pairs = [[1, 0]]

    n = 4
    preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
    pairs = [[1, 3], [0, 2]]

    print(sl.unhappyFriends(n, preferences, pairs))

    pass


if __name__ == "__main__":
    main()
