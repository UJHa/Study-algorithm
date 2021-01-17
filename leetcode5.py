# 내가 짠 방식
# class Solution(object):
#     def expand(self, s, left, right):
#         rs = s[left]
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             rs = s[left:right+1]
#             left -= 1
#             right += 1
#
#         return rs
#
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         if 1 == len(s) or s == s[::-1]:
#             return s
#
#         result = ''
#         for i in range(len(s)):
#             peven = self.expand(s, i, i + 1)
#             podd = self.expand(s, i, i + 2)
#             rtemp = max(peven, podd, key=len)
#             result = max(result, rtemp, key=len)
#
#         return result

# 교재 방식
class Solution(object):
    def expand(self, s, left, right):
        while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1

        return s[left+1:right-1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s)):
            result = max(result, self.expand(s, i, i + 1), self.expand(s, i, i + 2), key=len)

        return result

s = Solution()
# strs = "abcba"
# strs = "babad"
strs = "cbbd"
# print(strs[0:1])
# print('end['+s.longestPalindrome(strs)+']')
test = ''