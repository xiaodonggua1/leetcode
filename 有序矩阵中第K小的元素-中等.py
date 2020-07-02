"""
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

示例：

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。

提示：
你可以假设 k 的值永远是有效的，1 ≤ k ≤ n2 。
"""
"""
归并排序
二分查找
"""
from typing import List


def kthSmallest(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    result = []
    for i in range(n):
        for j in range(n):
            x = matrix[i][j]
            if len(result) == 0:
                result.append(x)
                continue
            for z in range(len(result)):
                if x <= result[z]:
                    result.insert(z, x)
                    break
                else:
                    if z == len(result) - 1:
                        result.append(x)
                        break

    return result[k - 1]


a = [
   [1, 2],
   [1, 3]
]
# print(a[0][1])
b = 3
print(kthSmallest(a, b))