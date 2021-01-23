class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        #for 정방향으로만 풀어보기
        # p = 1
        # result = []
        # for i in range(len(nums)):
        #     result.append(p)
        #     p *= nums[i]
        #
        # nums.reverse()
        #
        # p = 1
        # temp = []
        # for i in range(len(nums)):
        #     temp.append(p)
        #     p *= nums[i]
        #
        # temp.reverse()
        #
        # for i in range(len(result)):
        #     result[i] *= temp[i]
        #
        # return result

        #for 역방향으로 코드 정리 및 최적화
        p = 1
        result = []
        for i in range(len(nums)):
            result.append(p)
            p *= nums[i]

        p = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= p
            p *= nums[i]

        return result


s = Solution()

nums = [1,2,3,4]
print(111, s.productExceptSelf(nums))