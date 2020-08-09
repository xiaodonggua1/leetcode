"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""
from typing import List


def restoreIpAddresses(s: str) -> List[str]:
    ans = []
    segments = [0] * 4
    def dfs(id: int, start: int):
        # 找到了4段ip地址，遍历结束
        if id == 4:
            # 如果正好遍历完了字符串，那么这就是一种结果，否则就直接结束
            if start == len(s):
                ip = '.'.join(str(seg) for seg in segments)
                ans.append(ip)
            return

        # 如果没有找到4段ip地址但是却已经遍历完了字符串，那么直接结束
        if start == len(s):
            return

        # ip地址不能有前导0，即只能是1，而不能是01，所以如果遍历当前为0，那么这段ip就只能是0
        if s[start] == '0':
            segments[id] = 0
            dfs(id + 1, start + 1)

        address = 0
        for i in range(start, len(s)):
            address = address * 10 + int(s[i])
            if 0 < address <= 255:
                segments[id] = address
                dfs(id + 1, i + 1)
            else:
                break

    dfs(0, 0)
    return ans


# a = "25525511135"
a = "0000"
print(restoreIpAddresses(a))