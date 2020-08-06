#!/usr/bin/env python
# -*- encoding: utf-8 -*-   
# @Time    :  2020/8/6 下午5:46 
# @Author  :  TCL
"""
给定一组 互不相同 的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，
可拼接成回文串。

输入：["abcd","dcba","lls","s","sssll"]
输出：[[0,1],[1,0],[3,2],[2,4]]
解释：可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
示例 2：

输入：["bat","tab","cat"]
输出：[[0,1],[1,0]]
解释：可拼接成的回文串为 ["battab","tabbat"]
"""
from typing import List


def palindromePairs(words: List[str]) -> List[List[int]]:
    def findWord(s: str, left: int, right: int) -> int:
        return indices.get(s[left: right+1], -1)

    def isPalindrome(s: str, left: int, right: int) -> bool:
        return s[left: right + 1] == s[left: right + 1][::-1]

    indices = {word[::-1]: i for i, word in enumerate(words)}

    ret = []

    for i, word in enumerate(words):
        m = len(word)
        for j in range(m + 1):
            if isPalindrome(word, j, m - 1):
                left = findWord(word, 0, j - 1)
                if left != -1 and left != i:
                    ret.append([i, left])
            if j and isPalindrome(word, 0, j - 1):
                right = findWord(word, j, m - 1)
                if right != -1 and right != i:
                    ret.append([right, i])

    return ret


# a = ["abcd", "dcba", "lls", "s", "sssll"]
a = ["bat", "tab", "cat"]
print(palindromePairs(a))