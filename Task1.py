class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    
    pointerA = headA
    pointerB = headB
    
    while pointerA != pointerB:
        if pointerA:
            pointerA = pointerA.next
        else:
            pointerA = headB
        
        if pointerB:
            pointerB = pointerB.next
        else:
            pointerB = headA
    
    return pointerA