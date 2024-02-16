# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
1 -> 2 -> 3 -> 4를 예시로 설명
'''


class Solution:
    def swap(self, LN):
        if (LN == None) or (LN.next) == None: return

        # 1) LN.next.val은 두 번째 값을 뜻함
        # 2) 그걸 저장해두고,

        temp = LN.next.val
        LN.next.val = LN.val
        LN.val = temp

        LN = LN.next.next
        
        self.swap(LN)

    def swapPairs(self, head):

        self.swap(head)
        
        return head