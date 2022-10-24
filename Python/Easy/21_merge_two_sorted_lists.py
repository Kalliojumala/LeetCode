"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next


def solution(list1: ListNode, list2: ListNode) -> ListNode:
    ans = ListNode(0)
    curr = ans
    while list1 and list2:
        a = list1.val if list1 else 101
        b = list2.val if list2 else 101
        if a <= b:
            curr.next = ListNode(a)
            list1 = list1.next
            curr = curr.next
        else:
            curr.next = ListNode(b)
            list2 = list2.next
            curr = curr.next

    return ans.next
