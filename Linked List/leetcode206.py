from leetcode_import import *


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # 재귀를 통한 풀이
    # def reverse(self, node, prev=None):
    #     if not node:
    #         return prev
    #     nexts, node.next = node.next, prev
    #     return self.reverse(nexts, node)
    def reverseList(self, head):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 재귀를 통한 풀이
        # head = self.reverse(head)
        # return head

        # 반복을 사용한 풀이
        node, prev = head, None
        while node:
            nexts, node.next = node.next, prev
            prev, node = node, nexts

        return prev


s = Solution()

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

head1 = s.reverseList(head1)
while head1:
    print(head1.val)
    head1 = head1.next