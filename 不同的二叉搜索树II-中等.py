"""
给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。

输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generateTrees(n: int) -> List[TreeNode]:
    def helper(start, end):
        if start > end:
            return [None, ]
        allTrees = []
        for i in range(start, end + 1):
            leftTrees = helper(start, i - 1)
            rightTrees = helper(i + 1, end)

            for l in leftTrees:
                for r in rightTrees:
                    currTree = TreeNode(i)
                    currTree.left = l
                    currTree.right = r
                    allTrees.append(currTree)

        return allTrees

    return helper(1, n) if n else []


a = generateTrees(3)
print(a)