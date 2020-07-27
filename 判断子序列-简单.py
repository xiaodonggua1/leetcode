#!/usr/bin/env python
# -*- encoding: utf-8 -*-   
# @Time    :  2020/7/27 下午6:11 
# @Author  :  TCL
"""
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1:
s = "abc", t = "ahbgdc"

返回 true.

示例 2:
s = "axc", t = "ahbgdc"

返回 false.
"""


def isSubsequence(s: str, t: str) -> bool:
    n = len(t)
    m = len(s)
    if m == 0:
        return True
    j = 0
    for i in range(n):
        if t[i] == s[j]:
            j += 1
        if j == m:
            return True

    return False


a = ''
b = 'ahbgdc'
# a = 'axc'
# b = 'ahbgdc'
# a = 'b'
# b = 'c'
print(isSubsequence(a, b))