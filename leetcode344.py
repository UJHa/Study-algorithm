class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 방법 1
        s.reverse()
        # 방법 2
        # half_len = int(len(s) / 2)
        # for i in range(half_len):
        #     temp = s[i]
        #     s[i] = s[len(s) - 1 - i]
        #     s[len(s) - 1 - i] = temp

s = Solution()
stest = ["h","e","l","l","o"]
# stest = ["cde","cfc","abc"]
s.reverseString(stest)
print(stest)