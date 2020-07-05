"""
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
"""

def isMatch(s: str, p: str) -> bool:
    m = len(s)
    n = len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1) ]
    dp[0][0] = True

    for i in range(1, n + 1):
        if p[i - 1] == '*':
            dp[0][i] = True
        else:
            break

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] | dp[i][j - 1]
            if p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

    return dp[m][n]

a = 'aa'
b = '*'
print(isMatch(a, b))