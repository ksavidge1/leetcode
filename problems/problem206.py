"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(elements):
    head = ListNode(elements[0])
    current = head
    for value in elements[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        while current:
            next_node = current.next  # store next node
            current.next = prev  # reverse the current node's pointer
            prev = current  # move pointers one position ahead
            current = next_node
        return prev  # new head of the reversed list


def linked_list_to_list(head):
    elements = []
    current = head
    while current:
        elements.append(current.val)
        current = current.next
    return elements


input_test = [1,2,3,4,5]
linked_list = create_linked_list(input_test)
solution_obj = Solution()
output = solution_obj.reverseList(linked_list)
output_as_list = linked_list_to_list(output)


print(output_as_list)

