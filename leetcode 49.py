import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        groups = collections.defaultdict(list)

        for s in strs:
            groups[''.join(sorted(s))].append(s)

        return [g for g in groups.values()]


s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))