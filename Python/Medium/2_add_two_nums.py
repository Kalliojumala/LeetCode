# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwo(l1, l2):
    linked_sum = [ListNode(int(x)) for x in str(int("".join([str(x) for x in l1[::-1]])) + int("".join([str(x) for x in l2[::-1]])))[::-1]]
    for i in range(len(linked_sum)-1):
        linked_sum[i].next = linked_sum[i+1]

    return linked_sum

def addTwo_lazy(l1, l2):
    if len(l1) >= len(l2):
        x, long = len(l1), l1
        shorter = l2
        long = l1
    else:
        x, long = len(l2), l2
        shorter = l1
        
    lista = []
    extra = 0
    
    for i in range(x):
        if i < len(shorter):
            param_2 = shorter[i]
        else:
            param_2 = 0
            
        query = param_2 + long[i] + extra
    
        if query > 9:
            lista.append(ListNode(query % 10))
            extra = 1

        else:
            lista.append(ListNode(query))
            extra = 0

    if extra == 1:
        lista.append(ListNode(extra))

def addTwo_actual(l1, l2):
    #sum 2 linked lists into one
    carry = 0
    result = ListNode(0) #Dummy start, stripped from return/output
    current = result

    while l1 or l2 or carry != 0:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        col_sum = val1 + val2 + carry
        
        if col_sum > 9:     #carry is 1 or 0 (max values 9 + 9 + 1)
            carry = 1       #if col_sum > 9 we carry 1(10) to the next node and set col_sum - 10 to current node            
            col_sum -= 10
        else:
            carry = 0
        node = ListNode(col_sum) 
        current.next = node      #set value
        current = node           #next node == new created node
        l1 = l1.next if l1 else None 
        l2 = l2.next if l2 else None

    return result.next

l1 = ListNode(2,ListNode(4,ListNode(3, ListNode(1 , None))))
l2 = ListNode(5,ListNode(6,ListNode(4, None)))
x = addTwo_actual(l1, l2)

print(x)
while x:
    print(x.val)
    x =  x.next

