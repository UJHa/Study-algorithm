class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 브루트 포스 풀이
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         sum = nums[i]+nums[j]
        #         if sum is target:
        #             return [i,j]



        # 두 수의 차로 풀이 1
        # for i,n in enumerate(nums):
        #     temp_num = target - n
        #
        #     if temp_num in nums[i+1:]:
        #         temp_index = nums.index(temp_num)
        #         return [i, temp_index]

        # 두 수의 차로 풀이 2(속도 개선)
        numsmap = {}
        for i,n in enumerate(nums):
            numsmap[n] = i

        for i,n in enumerate(nums):
            temp_num = target - n

            if temp_num in numsmap and numsmap[temp_num] is not i:
                return [i, numsmap[temp_num]]

        # 두 수의 차로 풀이 3(풀이 2 코드 개선)
        # numsmap = {}
        # for i, n in enumerate(nums):
        #     temp_num = target - n
        #
        #     if temp_num in numsmap and numsmap[temp_num] is not i:
        #         return [i, numsmap[temp_num]]
        #     numsmap[n] = i


s = Solution()

nums = [-1,-2,-3,-4,-5]
target = 9
print(s.twoSum(nums, target))