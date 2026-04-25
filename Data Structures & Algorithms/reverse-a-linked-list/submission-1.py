# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        
        if not nums:
            return None
        
        nums.reverse()
        ans = ListNode(nums[0])
        curr = ans

        for i in range(1, len(nums)):
            curr.next = ListNode(nums[i])
            curr = curr.next

        return ans