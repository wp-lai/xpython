"""
Task:
    Merge k sorted linked lists and return it as one sorted list.

Examples:
>>> l1 = nums_2_list([10, 20, 30])
>>> l2 = nums_2_list([15, 25, 28])
>>> list_2_nums(merge_k_lists([l1, l2]))
[10, 15, 20, 25, 28, 30]
"""
import heapq
from typing import List, Iterable


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def nums_2_list(nums: Iterable[int]) -> ListNode:
    head = ListNode(None)
    cur = head
    for num in nums:
        cur.next = ListNode(num)
        cur = cur.next
    return head.next


def list_2_nums(head: ListNode) -> List[int]:
    return list(NodeIter(head))


class NodeIter(object):

    def __init__(self, node):
        self.cur = node

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur is None:
            raise StopIteration
        else:
            val = self.cur.val
            self.cur = self.cur.next
            return val


def merge_k_lists(lists: List[ListNode]) -> ListNode:
    lists = [NodeIter(head) for head in lists]
    merged = heapq.merge(*lists)
    head = nums_2_list(merged)
    return head
