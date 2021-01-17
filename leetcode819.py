import re
import collections
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                 if word not in banned]

        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1

        return max(counts, key=counts.get)


s = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
print(s.mostCommonWord(paragraph, ["hit"]))