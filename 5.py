#coding:utf-8
'''
求一个字符串的最大回文字符
input: "babad"
output: "aba" 或 "bab"
暴力破解：遍历每一个字串，判断是否回文
两个步骤：
1. 循环遍历字符串
2. 中心向两边扩散判断是否回文
    -> 分为两种情况，一种是奇数长度，一种偶数长度
'''

class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        maxL, maxR, max_len = 0, 0, 0
        for i in range(n):
            #回文是偶数
            start = i
            end = i + 1
            while start>=0 and end<n:
                if s[start] == s[end]:
                    if end - start + 1 > max_len:
                        max_len = end - start + 1
                        maxL = start
                        maxR = end
                    start -= 1
                    end += 1
                else: break

            #回文是奇数
            start = i - 1
            end = i + 1
            while start>=0 and end<n:
                if s[start] == s[end]:
                    if end - start + 1 > max_len:
                        max_len = end - start + 1
                        maxL = start
                        maxR = end
                    start -= 1
                    end += 1
                else: break

        return s[maxL:maxR+1]

string = Solution().longestPalindrome("abba")
print string