'''
Problem Assigned on: 09 March 2022 
Source : LeetCode

Given the head of a sorted linked list, 
delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.
Return the linked list sorted as well.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def build_nodes(self,values):
            root = ListNode(-100000)
            head = root
            for k,v in sorted(values.items() , key = lambda item: item[0]):
                        if root.val is -100000:
                                root.val = k
                        else:
                                head.next = ListNode(k) 
                                head = head.next
            return root
        
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
             return 
            
        values = {}
        root = head
        
        while root:
                if root.val not in values:
                      values[root.val] = 1
                else: 
                      values[root.val] +=1
                root = root.next
                
        value_c = values.copy()
        for k,v in value_c.items():
                 if v > 1:
                    del values[k]
        print(values)
        if len(values) > 0:
               return self.build_nodes(values)
        else:    
               return 
            
              