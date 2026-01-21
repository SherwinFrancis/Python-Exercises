class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    l1 = list1 
    l2 = list2 
    returnList = ListNode(1)
    current = returnList

    while l1 and l2:
        if l1.val < l2.val:
            current.next = ListNode(l1.val)
            current = current.next 
            l1 = l1.next 
        else:
            current.next = ListNode(l2.val)
            current = current.next 
            l2 = l2.next
        
    if l1:
            current.next = l1
    else:
        current.next = l2   

    return returnList.next
