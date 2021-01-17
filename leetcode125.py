class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        temp = ''
        for c in s:
            if c.isalnum():
                temp += c

        return temp == temp[::-1]
        # s = s.upper()
        # p1 = 0
        # p2 = len(s) - 1
        # while p1 < p2:
        #     while not s[p1].isalnum():
        #         p1 += 1
        #         if p1 == len(s):
        #             break
        #
        #     while not s[p2].isalnum():
        #         p2 -= 1
        #         if p2 == 0:
        #             break
        #
        #     if not p1 < p2:
        #         return True
        #
        #     if s[p1] != s[p2]:
        #         return False
        #
        #     p1 += 1
        #     p2 -= 1
        # return True


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
# print(s.isPalindrome(".,"))
print('test string'[::-1])