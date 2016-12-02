#coding:utf-8
"""
求一个字符串的最大不包含重复字符的子串的长度
"""
#时间复杂度O(n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
    	length = 0
    	dict = {}
    	pre, after = 0, 0

    	while(after < len(s)):
    
    		if s[after] in dict:
    			l = after - pre;
	    		if l > length:
	    			length = l
    			i = dict.get(s[after])
    			pre = max(i, pre)
    		
    		dict[s[after]] = after + 1
    		after += 1

    	return max(length, after - pre)

solution = Solution()
s = "abbc"
length = solution.lengthOfLongestSubstring(s)
print length