"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution_double_pass(head: ListNode, n: int) -> ListNode:
    #two pass implementation
    head_len = head
    lenght = 0
    while head_len:
        lenght += 1
        head_len = head_len.next
    
    curr = head
    prev = None
    
    if lenght == n:
        return curr.next

    while head:
        if lenght == n:
            prev.next = curr.next
            break

        lenght -= 1
        prev = curr
        curr = curr.next
    
    return head

def solution_single_pass(head: ListNode, n: int) -> ListNode:
    dummy_head = head       
    lenght = 0
    stack = []          
    while dummy_head:
        lenght += 1
        stack.append(dummy_head)
        dummy_head = dummy_head.next
    
    if lenght == n:                             #want to delete first item from the left, return head.next
        return head.next 
    
    index_to_remove = lenght - n                #ListNode to remove in stack

    if index_to_remove == len(stack) - 1:       #This check prevents index error if removing last item from list by setting itr - 1 to none 
        stack[index_to_remove - 1].next = None
        return head
   
    stack[index_to_remove - 1].next = stack[index_to_remove + 1] #Delete the wanted index by setting its parents 'next' value to its child/next

    return head
    
    


if __name__ == '__main__':
    inp = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    inp_2 = ListNode(1, ListNode(2))
    x = solution_single_pass(inp, 1)
    while x:
        print(x.val)
        x = x.next
     
       