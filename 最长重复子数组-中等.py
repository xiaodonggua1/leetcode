"""
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例：

输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1] 。
 
提示：
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""
from typing import List


def findLength(A: List[int], B: List[int]) -> int:
    n = len(A)
    m = len(B)
    dp = [[0 for col in range(n)] for row in range(m)]
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                if i >= 1 and j >= 1:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 1

    return max(max(row) for row in dp)


a = [1, 2, 3, 2, 1]
b = [3, 2, 1, 4, 7]
print(findLength(a, b))
