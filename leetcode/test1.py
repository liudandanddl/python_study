#!/usr/bin/env python
# coding=utf-8
import sys

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


def findMinArrowShots(points):
    """
    几箭可以射爆气球，输入的每个二维数组都是气球的宽度，若有一个气球的直径的开始和结束坐标为 xstart，xend，且满足xstart ≤ x ≤ xend，则该气球会被引爆。
    输入:[[10,16], [2,8], [1,6], [7,12]]
    输出:2
    解释:对于该样例，我们可以在x = 6（射爆[2,8],[1,6]两个气球）和 x = 11（射爆另外两个气球）。
    以第一个气球的终止位置为准，只要出现的气球起始位置小于这个气球的终止位置，代表可以一箭使这些气球全部爆炸；
    当出现一个气球的起始位置大于第一个气球的终止位置时再以这个气球的终止位置为准，找出所有可以再一箭爆炸的所有气球；以此类推。。。
    这道题目是活动选择问题(Activity-Selection Problem)的变形。活动选择问题是《算法导论》里面关于贪心算法的第一个问题。这个问题是这样的。
    有一组活动，每个活动都有一个开始时间S和结束时间F，假设一个人在同一时间只能参加一个活动，找出出一个人可以参加的最多的活动数量。
    :type points: List[List[int]]
    :rtype: int
    """
    points.sort(key=lambda x:x[1])  # 二维数组，按照第二个元素排序
    res = 0
    last_end = -sys.maxint  # python的INT类型最大值
    for p in points:
        if p[0] > last_end:
            last_end = p[1]
            res += 1
    return res