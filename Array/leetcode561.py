class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 1. 오름차순 정렬 후 2개씩 묶어서 min() 처리
        # nums.sort()
        # pair = []
        # sum = 0
        # for n in nums:
        #     pair.append(n)
        #     if len(pair) == 2:
        #         sum += min(pair)
        #         pair = []
        # return sum

        # 2. 오름차순 정렬 후 홀수 번째의 값 합치기(오름차순에서는 홀수 번째가 작은 수(min 결과값)가 되기 때문)
        nums.sort()

        min_sum = 0
        for i in range(0,len(nums)-1,2):
            min_sum += nums[i]

        return min_sum

        # 3. 2의 방법 Pythonic으로 축약하기
        # return sum(sorted(nums)[::2])


s = Solution()

# nums = [1,4,3,2]
nums = [6,2,6,5,1,2]
print(111, s.arrayPairSum(nums))