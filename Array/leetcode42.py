class Solution(object):
    # def find_right_index(self, index, height):
    #     temp_index = index + 1
    #     if temp_index == len(height):
    #         return index
    #
    #     while temp_index < len(height):
    #         if height[index] > height[temp_index]:
    #             temp_index += 1
    #         else:
    #             return temp_index
    #     return index + 1
    #
    # def trap(self, height):
    #     """
    #     :type height: List[int]
    #     :rtype: int
    #     """
    #
    #     result = 0
    #     l_index = 0
    #     while l_index < len(height):
    #         left_height = height[l_index]
    #         if left_height == 0:
    #             l_index += 1
    #             continue
    #
    #         # print(22, l_index)
    #         r_index = self.find_right_index(l_index, height)
    #         # print(33, r_index)
    #
    #         if l_index == r_index:
    #             break
    #
    #         right_height = height[r_index]
    #         limit_height = min(left_height,right_height)
    #         # 물 계산
    #         print(l_index, r_index,height[l_index + 1:r_index], limit_height)
    #         water_list = []
    #         for h in height[l_index + 1:r_index]:
    #             water_list += [limit_height - h]
    #             result += limit_height - h
    #         print(44444, water_list)
    #         l_index = r_index
    #     return result

    def trap(self, height):
        # 투 포인터 풀이(좌우 포인터)
        # if not height:
        #     return 0
        #
        # volume = 0
        # left, right = 0, len(height) - 1
        # left_max, right_max = height[left], height[right]
        #
        # while left < right:
        #     left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        #
        #     if left_max <= right_max:
        #         volume += left_max - height[left]
        #         left += 1
        #     else:
        #         volume += right_max - height[right]
        #         right -= 1
        #
        # return volume

        # 스택 활용한 풀이
        stack = []
        result = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if len(stack) == 0: # not len(stack)도 가능
                    break

                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                result += distance * waters
            stack.append(i)

        return result



s = Solution()

# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
print(111, s.trap(height))