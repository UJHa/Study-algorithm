# 문제 풀이 진행중..(나중에 재도전)
import collections
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        # 전체 연결점 개수 확인한다.
        # 개수가 적은 것 부터 처리한다
        # # 연결된 게 0개인 애들은 제외
        #

        # data init
        stones_share_list = []
        for i in range(len(stones)):
            stones_share_list.append(0)

        # set data(connecting count of stones)
        for i in range(len(stones)):
            check_stone = stones[i]
            connect_count = 0
            for j in range(len(stones)):
                if i is j:
                    continue
                if check_stone[0] is stones[j][0] or check_stone[1] is stones[j][1]:
                    connect_count += 1

            stones_share_list[i] = connect_count

        connect_sum = 0
        for share in stones_share_list:
            connect_sum += share

        if connect_sum is 0:
            return 0

        island = 0
        print(stones_share_list)
        for connect in stones_share_list:
            if connect is 0:
                island += 1
        print(island)
        return len(stones) - (island + 1)


s = Solution()

# temp_value = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2],[2,3]]
# temp_value = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# temp_value = [[0,0],[0,2],[1,1],[2,0],[2,2]]
temp_value = [[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]]
print(s.removeStones(temp_value))