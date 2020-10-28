# https://leetcode.com/problems/first-bad-version/
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            m = l + (r - l) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1

        if l != n + 1 and isBadVersion(l):
            return l
        else:
            return -1