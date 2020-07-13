"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
"""
from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    n = len(nums1)
    m = len(nums2)
    if n > m:
        short_list = nums2
        long_list = nums1
    else:
        short_list = nums1
        long_list = nums2
    intersect_list = []
    for i in short_list:
        if i in long_list:
            long_list.remove(i)
            intersect_list.append(i)

    return intersect_list


# a = [1, 2, 2, 1]
a = [4, 9, 5]
# b = [2, 2]
b = [9, 4, 9, 8, 4]
print(intersect(a, b))