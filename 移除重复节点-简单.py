"""
编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

示例1:

 输入：[1, 2, 3, 3, 2, 1]
 输出：[1, 2, 3]
示例2:

 输入：[1, 1, 1, 1, 2]
 输出：[1, 2]
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeDuplicateNodes(head: ListNode) -> ListNode:
    exist = []
    l = ListNode(None)
    l1 = l
    while head:
        if head.val not in exist:
            exist.append(head.val)
            l1.next = ListNode(None)
            l1 = l1.next
            l1.val = head.val
        head = head.next

    return l.next

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(3)
a.next.next.next.next = ListNode(2)
a.next.next.next.next.next = ListNode(1)

b = removeDuplicateNodes(a)
while b:
    print(b.val)
    b = b.next

