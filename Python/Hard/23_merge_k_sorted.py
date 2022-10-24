"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Constraints:

    k == lists.length
    0 <= k <= 104
    0 <= lists[i].length <= 500
    -104 <= lists[i][j] <= 104
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 104.

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#naive approach
def solution(lists: list) -> ListNode:
    #destructure the lists and create a single linked list out of the stack
    stack = []
    for i in lists:
        while i:
            stack.append(i.val)
            i = i.next

    stack.sort()
    
    head = ListNode(0)
    curr = head
    for i in stack:
        curr.next = ListNode(i)
        curr = curr.next

    return head.next

#TODO:
#More efficient solution

if __name__ == '__main__':
    a = ListNode(1,ListNode(4,ListNode(5)))
    b = ListNode(1,ListNode(3,ListNode(4)))
    c = ListNode(2,ListNode(6))

    linked, stack = solution([a,b,c])

    while linked:
        print(linked.val)
        linked = linked.next

    print(stack)