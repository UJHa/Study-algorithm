from leetcode_import import *


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # 예외에 대한 처리+첫 값 비교를 통한 재귀 처리
        # if not l1 and not l2:
        #     return None
        # elif not l1:
        #     return l2
        # elif not l2:
        #     return l1
        #
        # if l1.val < l2.val:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        #     return l1
        # else:
        #     l2.next = self.mergeTwoLists(l1, l2.next)
        #     return l2

        # 코드 짧게 만든 풀이 1
        # if not l1:                          # l1 기준으로 반환하기 위한 l1,l2 값 교체
        #     l1, l2 = l2, l1
        #
        # if l1 and l2 and l1.val > l2.val:   # l1의 첫 값이 작도록 l1,l2 값 교체
        #     l1, l2 = l2, l1
        #
        # if l1:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        # return l1

        # 코드 더! 짧게 만든 풀이 2
        # if not l1 or (l1 and l2 and l1.val > l2.val):
        #     l1, l2 = l2, l1
        #
        # if l1:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        # return l1

        # 코드 더! 짧게 만든 풀이 3
        # 풀이 2에서의 not l1과 l1은 동시에 발생할 수 없으므로 후 조건인 'l1 and'를 제거
        # if not l1 or (l2 and l1.val > l2.val):
        #     l1, l2 = l2, l1
        #
        # if l1:
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        # return l1

        # 결과 제출 풀이
        # 예외에 대한 조건 처리 + l1, l2 swap으로 하나의 재귀로 코드 정리
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1

        if l1.val > l2.val:
            l1, l2 = l2, l1

        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1


s = Solution()

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(4)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next = ListNode(4)
print(111, s.mergeTwoLists(head1, head2))
while head1:
    print(head1.val)
    head1 = head1.next