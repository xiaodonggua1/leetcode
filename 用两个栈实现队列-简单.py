"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：

1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用
"""

class CQueue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def appendTail(self, value: int) -> None:
        self.stack1.push(value)

    # def deleteHead(self) -> int:
    #     if self.stack1.is_empty():
    #         return -1
    #
    #     while not self.stack1.is_empty():
    #         self.stack2.push(self.stack1.pop())
    #
    #     result = self.stack2.pop()
    #     while not self.stack2.is_empty():
    #         self.stack1.push(self.stack2.pop())
    #
    #     return result

    def deleteHead(self) -> int:
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())

            result = self.stack2.pop()
        else:
            result = self.stack2.pop()

        return result


class Stack:

    def __init__(self):
        self.list = []

    def is_empty(self):
        return len(self.list) == 0

    def push(self, value: int) -> None:
        self.list.append(value)

    def pop(self) -> int:
        if self.is_empty():
            return -1

        return self.list.pop()

    def top(self) -> int:
        if self.is_empty():
            return -1

        return self.list[-1]


# Your CQueue object will be instantiated and called as such:
obj = CQueue()
obj.appendTail(5)
obj.appendTail(2)
print(obj.deleteHead())
print(obj.deleteHead())
print(obj.deleteHead())