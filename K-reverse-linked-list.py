# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def reverseList(self, A, B):
        start = A
        p1 = A
        p2 = A
        pNext = A
        bStart = False
        end = None
        while ( p2 != None):
            for i in range(B-1):
                p2 = p2.next
                if (p2 == None):
                    break
            if ( p2 != None):
                pNext = p2.next
            else:
                pNext = None

            localStart, localEnd = self.reverse(p1, p2)
            if (bStart == False):
                start = localStart
                bStart = True
                end = localEnd
            else:
                end.next = localStart
                end = localEnd
                
            p1 = pNext
            p2 = p1
        end.next = None
        return start        

    def reverse(self, p, e):
        if (p == None):
            return
        
        p1 = p
        p2 = p1.next

        if ( p2 == None):
            start = p1
            end = p1
            return (start, end)
            
        p3 = p2.next
        while(p1 != e):           
            p2.next = p1
            p1  = p2
            p2 = p3
            if (p1 == None) or ( p2 == None):
                break
            p3 = p2.next
        
        start = p1
        end = p
        return (start, end)