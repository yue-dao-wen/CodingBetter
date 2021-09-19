# -*- coding: utf-8 -*-
"""
@author: Me
@time: 2021/9/1 22:47
@description:
"""


class Solution:
    def compareVersion(self, version1: str, version2: str):
        i, j = 0, 0
        v1 = version1.split(".")
        v2 = version2.split(".")

        while i < len(v1) and j < len(v2):
            num1 = int(v1[i])
            num2 = int(v2[j])
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
            i += 1
            j += 1

        if i == len(v1):
            while j < len(v2):
                num2 = int(v2[j])
                if num2 != 0:
                    return -1
                j += 1
            return 0


        if j == len(v2):
            while i < len(v1):
                num1 = int(v1[i])
                if num1 != 0:
                    return 1
                i += 1
            return 0
            pass

        return 0


def main():
    sl = Solution()
    version1 = "1.01"
    version2 = "1.001"

    version1 = "1.001"
    version2 = "1.01"

    version1 = "1.0"
    version2 = "1.0.0"

    version1 = "1.0.0"
    version2 = "1.0"

    version1 = "0.1"
    version2 = "1.1"

    version1 = "1.1"
    version2 = "0.1"

    version1 = "1.0.1"
    version2 = "1"

    version1 = "1"
    version2 = "1.0.1"

    version1 = "7.5.2.4"
    version2 = "7.5.3"

    version1 = "7.5.3"
    version2 = "7.5.2.4"

    print(sl.compareVersion(version1, version2))

    pass


if __name__ == "__main__":
    main()
