#!/usr/bin/env python
# -*- encoding: utf-8 -*-   
# @Time    :  2020/8/5 下午5:52 
# @Author  :  TCL
"""
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，
聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，
房屋将自动报警。计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.

输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def rob(root: TreeNode) -> int:
    def _rob(root):
        if not root: return 0, 0

        left = _rob(root.left)
        right = _rob(root.right)

        # 偷当前节点，则左右节点都不能偷
        v1 = root.val + left[1] + right[1]
        # 不偷当前节点，则取左右子树最大值
        v2 = max(left) + max(right)

        return v1, v2

    return max(_rob(root))


a = TreeNode(3)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.right = TreeNode(3)
a.right.right = TreeNode(1)
print(rob(a))



