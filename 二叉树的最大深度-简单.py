#!/usr/bin/env python
# -*- encoding: utf-8 -*-   
# @Time    :  2020/7/28 下午5:11 
# @Author  :  TCL
"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(root: TreeNode) -> int:
    if root is None:
        return 0

    return max(maxDepth(root.left), maxDepth(root.right)) + 1