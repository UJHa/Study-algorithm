class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        #하나씩 다해보기 >> n^3으로 "Time Limit Exceeded"로 해결 불가
        # if len(nums) < 3:
        #     return []
        #
        # output = []
        # for i,n in enumerate(nums):
        #     print('####',i, n)
        #     for j,m in enumerate(nums[i+1:]):
        #         print('$$$$',j, m)
        #         for k,l in enumerate(nums[i+j+2:]):
        #             print('%%%%',k, l)
        #             if n+m+l == 0:
        #                 print('====')
        #                 temp = [n,m,l]
        #                 temp.sort()
        #                 if temp not in output:
        #                     output += [temp]
        # return output

        # 세 수의 차로 풀이해보기(실패)
        # if len(nums) < 3:
        #     return []
        #
        # print(nums)
        # print(nums[0:])
        # sumlist = []
        # for i, num1 in enumerate(nums):
        #     goalsum = 0 - num1
        #     print('$$$$',num1)
        #     for j,num2 in enumerate(nums[i+1:]):
        #         print('%%%%', num2)
        #         goal_num3 = goalsum - num2
        #         if goal_num3 in nums[i+j+1:]:
        #             print('^^^^', nums[num2+1:])
        #             temp = [num1, num2, goal_num3]
        #             temp.sort()
        #             if temp not in sumlist:
        #                 sumlist += [temp]
        # return sumlist

        # 좌우 포인터로 풀이하기
        nums.sort()
        results = []

        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1,len(nums) - 1

            while left < right:
                print(i, left, right)
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results



s = Solution()

nums = [-1,0,1,2,-1,-4]
# nums = [1,2,-2,-1]
# nums = [-13,5,13,12,-2,-11,-1,12,-3,0,-3,-7,-7,-5,-3,-15,-2,14,14,13,6,-11,-11,5,-15,-14,5,-5,-2,0,3,-8,-10,-7,11,-5,-10,-5,-7,-6,2,5,3,2,7,7,3,-10,-2,2,-12,-11,-1,14,10,-9,-15,-8,-7,-9,7,3,-2,5,11,-13,-15,8,-3,-7,-12,7,5,-2,-6,-3,-10,4,2,-5,14,-3,-1,-10,-3,-14,-4,-3,-7,-4,3,8,14,9,-2,10,11,-10,-4,-15,-9,-1,-1,3,4,1,8,1]
print(111, s.threeSum(nums))