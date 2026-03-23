class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    
    pointerA = headA
    pointerB = headB
    
    while pointerA != pointerB:
        if ptrA:
            ptrA = ptrA.next
        else:
            ptrA = headB
        
        if ptrB:
            ptrB = ptrB.next
        else:
            ptrB = headA
    
    return ptrA