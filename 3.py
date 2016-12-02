#coding:utf-8
"""
求一个字符串的最大不包含重复字符的子串的长度
"""
# 时间复杂度O(min(m, n)), 最差 O(2n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        """

        length = 0
        i, j = 0, 0
        x = set()

        while(j<len(s)):
            if s[j] not in x:
                l = j - i + 1
                if l > length:
                    length = l
                x.add(s[j])
                j += 1
            else:
                x.remove(s[i])
                i += 1
        return length

solution = Solution()
s = "abb"
length = solution.lengthOfLongestSubstring(s)
print length