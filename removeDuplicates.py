class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        if head.val == head.next.val:
            #print('Case 1',head)
            head=self.deleteDuplicates(head.next)
            return head
        else:
            #print('Case 2',head)
            head.next = self.deleteDuplicates(head.next)
            return head

        