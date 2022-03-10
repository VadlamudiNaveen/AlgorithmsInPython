'''
Problem Assigned on: 07-March-2022

Source: LeetCode 

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    import bisect
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case to handle the None Values        
        if list1 is None and list2 is None:
            return
        
        # O (Log N) Tc to Sort the Sorted List that arrives from multiple lists.
        def get_val(head,res):
             while head:
                bisect.insort(res,head.val)
                head = head.next

        res = []
        get_val(list1,res)
        get_val(list2,res)
        
        # O(N) Tc to Build the Nodes Back Again
        root = ListNode(res.pop(0))
        ptr = root
        while len(res) > 0:
                ptr.next = ListNode(res.pop(0))
                ptr = ptr.next
        return root        
        