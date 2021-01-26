from leetcode_import import *
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 리스트 변환 후 투 포인터 방식
        # node = head
        # s = []
        # while node is not None:
        #     s.append(node.val)
        #     node = node.next
        #
        # left = 0
        # right = len(s)-1
        # while left <= right:
        #     if s[left] == s[right]:
        #         left += 1
        #         right -= 1
        #     else:
        #         return False
        # return True

        # 리스트 변환 후 pop 함수 활용한 처리
        # node = head
        # s = []
        # while node is not None:
        #     s.append(node.val)
        #     node = node.next
        #
        # while len(s) > 1:
        #     if s.pop(0) != s.pop():
        #         return False
        # return True
        # deque 변환 후 pop 함수 활용한 처리
        # node = head
        # s = collections.deque()
        # while node is not None:
        #     s.append(node.val)
        #     node = node.next
        #
        # while len(s) > 1:
        #     if s.popleft() != s.pop():
        #         return False
        # return True
        # 런너를 이용한 풀이
        slow = fast = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next

            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        # rev = rev.next
        while rev and rev.val == slow.val:
            rev, slow = rev.next, slow.next
        return not rev







s = Solution()

head = ListNode(1, ListNode(1))
print(111, s.isPalindrome(head))
print(1 is 1)
print(-129 is -129)