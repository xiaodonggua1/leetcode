#!/usr/bin/env python
# -*- encoding: utf-8 -*-   
# @Time    :  2020/8/4 下午5:31 
# @Author  :  TCL
"""
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]

给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
"""
import collections
from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    edges = collections.defaultdict(list)
    visited = [0] * numCourses
    result = []
    valid = True

    for info in prerequisites:
        edges[info[1]].append(info[0])

    def dfs(u: int):
        nonlocal valid
        visited[u] = 1
        for v in edges[u]:
            if visited[v] == 0:
                dfs(v)
                if not valid:
                    return
            elif visited[v] == 1:
                valid = False
                return
        visited[u] = 2
        result.append(u)

    for i in range(numCourses):
        if valid and not visited[i]:
            dfs(i)

    return valid


a = 2
# b = [[1, 0]]
b = [[1, 0], [0, 1]]
print(canFinish(a, b))