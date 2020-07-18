"""
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false
"""
def isInterleave(s1: str, s2: str, s3: str) -> bool:
    m = len(s1)
    n = len(s2)
    t = len(s3)
    if m + n != t:
        return False
    dp = [[False] * (n + 1) for _ in range(m+1)]
    dp[0][0] = True
    for i in range(m + 1):
        for j in range(n + 1):
            p = i + j - 1
            if i > 0:
                dp[i][j] |= dp[i - 1][j] and s1[i - 1] == s3[p]
            if j > 0:
                dp[i][j] |= dp[i][j - 1] and s2[j - 1] == s3[p]

    return dp[-1][-1]


a = 'aabcc'
b = 'dbbca'
c = 'aadbbcbcac'
print(isInterleave(a, b, c))