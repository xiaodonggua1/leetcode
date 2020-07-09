"""
哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。
像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。
在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，
不过，有些词没在词典里。假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，
返回未识别的字符数。

输入：
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
输出： 7
解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。
"""
from typing import List


def respace(dictionary: List[str], sentence: str) -> int:
    dp = list(range(len(sentence) + 1))
    dp[0] = 0
    for i in range(1, len(sentence) + 1):
        dp[i] = dp[i - 1] + 1
        for j in range(i):
            if sentence[j:i] in dictionary:
                dp[i] = min(dp[i], dp[j])

    return dp[-1]


a = ["vprkj", "sqvuzjz", "ptkrqrkussszzprkqrjrtzzvrkrrrskkrrursqdqpp", "spqzqtrqs", "rkktkruzsjkrzqq",
     "rk", "k", "zkvdzqrzpkrukdqrqjzkrqrzzkkrr", "pzpstvqzrzprqkkkd", "jvutvjtktqvvdkzujkq", "r", "pspkr",
     "tdkkktdsrkzpzpuzvszzzzdjj", "zk", "pqkjkzpvdpktzskdkvzjkkj", "sr",
     "zqjkzksvkvvrsjrjkkjkztrpuzrqrqvvpkutqkrrqpzu"]

b = "rkktkruzsjkrzqqzkvdzqrzpkrukdqrqjzkrqrzzkkrr"

# a = ["looked", "just", "like", "her", "brother"]
# b = "jesslookedjustliketimherbrother"

print(respace(a, b))