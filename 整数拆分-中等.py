#!/usr/bin/env python
# -*- encoding: utf-8 -*-   
# @Time    :  2020/7/30 下午4:44 
# @Author  :  TCL
"""
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。
"""


def integerBreak(n: int) -> int:
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        for j in range(1, i):
            dp[i] = max(dp[i], j * (i - j), j * dp[i - j])

    return dp[n]


a = 10
print(integerBreak(a))