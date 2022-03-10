'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

T1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

T2: 
Input: l1 = [0], l2 = [0]
Output: [0]

T3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

T4:
[2,4,9]
[5,6,4,9]
output:[7,0,8]
[7,0,4,0,1]
[8,9,9,9,0,0,0,1]


'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getValue(self,head,res):
            values = []
            while head:
                values.append(head.val)
                head = head.next
            values = [str(i) for i in values[::-1]]
            res.append(int(''.join(values)))
            
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return
        res = []
        self.getValue(l1,res)
        self.getValue(l2,res)
        res = [int(char) for char in str(sum(res))]
        root = ListNode(-10000)
        head = root
        for val in res[::-1]:
                if root.val is -10000:
                        root.val = val
                else: 
                        head.next = ListNode(val)
                        head = head.next
        return root