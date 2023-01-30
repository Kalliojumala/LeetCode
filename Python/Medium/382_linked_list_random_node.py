from random import randint

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head: ListNode):
    
        self.range = {}
        self.idx = 0
        while head:
            self.range[self.idx] = head.val
            head = head.next
            self.idx += 1

    def getRandom(self) -> int:
        
        return self.range[randint(0, self.idx - 1)]