# -*- coding: utf-8 -*-
"""
@author: Me
@time: 2021/8/31 23:06
@description:
"""
from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int):
        book_dict = {}
        for book in bookings:
            f, t, s = book[:]
            if t < f:
                f, t = t, f
            for b in range(f, t + 1):
                book_dict[b] = book_dict.get(b, 0) + s

        ans = []
        for b in range(n+1):
            if b in book_dict:
                ans.append(book_dict[b])

        return ans


def main():
    sl = Solution()
    books = [[2, 2, 30], [2, 2, 45]]
    n = 2
    print(sl.corpFlightBookings(books, n))
    pass


if __name__ == "__main__":
    main()
