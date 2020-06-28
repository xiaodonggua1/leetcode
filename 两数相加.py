"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    list1 = []
    list2 = []
    while l1:
        list1.append(str(l1.val))
        l1 = l1.next
    while l2:
        list2.append(str(l2.val))
        l2 = l2.next
    list1.reverse()
    list2.reverse()
    num1 = int(''.join(list1))
    num2 = int(''.join(list2))
    num_sum = str(num1 + num2)[::-1]
    result = ListNode(int(num_sum[0]))
    result2 = result
    for i in range(len(num_sum)):
        if i > 0:
            result2.next = ListNode(int(num_sum[i]))
            result2 = result2.next

    return result


a = ListNode(2)
a.next = ListNode(4)
a.next.next = ListNode(3)
b = ListNode(5)
b.next = ListNode(6)
b.next.next = ListNode(4)
c = addTwoNumbers(a, b)
print(c.val)
print(c.next.val)
print(c.next.next.val)