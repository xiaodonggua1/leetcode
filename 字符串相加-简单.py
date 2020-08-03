#!/usr/bin/env python
# -*- encoding: utf-8 -*-   
# @Time    :  2020/8/3 下午4:31 
# @Author  :  TCL
"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
"""


# def addStrings(num1: str, num2: str) -> str:
#     if len(num1) >= len(num2):
#         long, short = num1, num2
#     else:
#         long, short = num2, num1
#     n = len(long)
#     short = short.zfill(n)
#     extra = 0
#     result = []
#     for i in range(n):
#         j = n - i - 1
#         sum = int(long[j]) + int(short[j]) + extra
#         result.insert(0, str(sum % 10))
#         if sum >= 10:
#             if i == n - 1:
#                 result.insert(0, '1')
#             extra = 1
#         else:
#             extra = 0
#     return ''.join(result)

def addStrings(num1: str, num2: str) -> str:
    i, j, extra, ans = len(num1) - 1, len(num2) - 1, 0, []

    while i >= 0 or j >= 0 or extra:
        x = int(num1[i]) if i >= 0 else 0
        y = int(num2[j]) if j >= 0 else 0
        result = x + y + extra
        ans.insert(0, str(result % 10))
        extra = result // 10
        i -= 1
        j -= 1

    return ''.join(ans)

a = '199'
b = '199'
# a = '1'
# b = '9'
print(addStrings(a, b))