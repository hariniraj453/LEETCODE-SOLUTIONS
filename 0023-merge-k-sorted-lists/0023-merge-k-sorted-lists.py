class Solution:
    def mergeKLists(self, lists):
        nodes = []
        for head in lists:
            while head:
                nodes.append(head)
                head = head.next

        nodes.sort(key=lambda x: x.val)

        dummy = curr = ListNode(0)
        for node in nodes:
            curr.next = node
            curr = curr.next
        curr.next = None
        return dummy.next