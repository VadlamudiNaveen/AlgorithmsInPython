'''
Problem Assigned On: 11 March 2022
Given the head of a linked list, rotate the list to the right by k places.

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Input: head = [0,1,2], k = 4
Output: [2,0,1]

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def build(self, res):
            root = ListNode(-1000)
            head = root
            # O(N) to build the List
            for val in res:
                    if root.val == -1000:
                         root.val = val
                    else:   
                            head.next = ListNode(val)
                            head = head.next
            return root
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return
        res = []
        # O(N) to iterate over the Linked List
        while head:
                res.append(head.val)
                head = head.next
                
        # O(N % K =~ M)
		# Rotating the Linked List Logic
        for i in range(k % len(res)):
                res = [res.pop()] + res
        
        return self.build(res)