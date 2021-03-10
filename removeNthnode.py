# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import Queue
class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    if n == 0:
        return head
    if head.next == None:
        if n == 1:
            head.val = ''
            return head
        else:
            head
    iterate = head.next
    q= Queue(maxsize=n+1)
    q.put(head)
    while iterate.next:
        if q.full():
            q.get()
        q.put(iterate)
        iterate=iterate.next
    if q.full():
        q.get()
    q.put(iterate)
    node = q.get() 
    if node == head and q.qsize()== n-1:
            head = head.next
    else:
        if n==1:
            node.next = None
        else:
            q.get()
            node.next = q.get()
    return head   

