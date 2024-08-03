class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative Solution
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next
    
# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy = ListNode()
    cur = dummy
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next  

def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)


solution = Solution()
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
result = solution.mergeTwoLists(list1, list2)
print_linked_list(result)