class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next  # Step 1: Save next
            curr.next = prev # Step 2: Reverse link
            prev = curr      # Step 3: Move prev forward
            curr = nxt       # Step 4: Move curr forward
            
        return prev  # New head