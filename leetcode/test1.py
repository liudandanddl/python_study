#!/usr/bin/env python
# coding=utf-8
__author__ = 'ldd'


def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    Input:s: "cbaebabacd" p: "abc"  从s中查找有多少个p
    Output: [0, 6]
    Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".
    """
    res = [];  sdic = {};  pdic = {}
    ls = len(s);  lp = len(p)
    for i in s[:lp]:
        sdic[i] = sdic.get(i, 0)+1
    for i in p:
        pdic[i] = pdic.get(i, 0)+1
    i = 0
    while i < ls-lp:
        if sdic == pdic:
            res.append(i)
        sdic[s[i]] -= 1  # 删除s的第一个元素
        if sdic[s[i]] == 0:
            sdic.pop(s[i])  # 删除key
        sdic[s[i+lp]] = sdic.get(s[i+lp], 0)+1
        i += 1
    if sdic == pdic:
        res.append(i)
    return res