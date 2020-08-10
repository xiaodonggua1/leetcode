#!/usr/bin/env python
# -*- encoding: utf-8 -*-   
# @Time    :  2020/8/10 下午5:02 
# @Author  :  TCL
"""
给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。

重复出现的子串要计算它们出现的次数。

输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

请注意，一些重复出现的子串要计算它们出现的次数。

另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。

输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
"""


def countBinarySubstrings(s: str) -> int:
    i, j = 0, 1
    num = 0
    while j <= len(s) - 1:
        if (s[i] == '0' and s[j] == '1') or (s[i] == '1' and s[j] == '0'):
            num += 1
            left, right = i - 1, j + 1
            while left >= 0 and right <= len(s) - 1:
                if s[left] == s[i] and s[right] == s[j]:
                    num += 1
                else:
                    break
                left -= 1
                right += 1
        i += 1
        j += 1

    return num

# a = '00110011'
# a = '10101'
a = '100111001'
print(countBinarySubstrings(a))