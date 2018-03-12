#!/usr/bin/env python
# coding=utf-8
from collections import Counter
import re

__author__ = 'ldd'


def trailingZeroes(n):
    """
    求阶乘结果尾部0的个数.0是由2*5所得，计算能被多少个5，25，125.。。。。整除
    :type n: int
    :rtype: int
    """
    return 0 if n==0 else n/5 +trailingZeroes(n/5)


def hammingWeight(n):
    """
    返回数字n变成二进制数后有多少个1
    :type n: int
    :rtype: int
    """
    str = bin(n)  # 0b1011  将整数转成二进制
    str = str[2:]
    return str.count('1')


def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rty
    """
    s1 = {}
    t1 = {}
    for i in range(0, len(s), 1):
        if s[i] not in s1.keys():
            s1[s[i]] = [i]
        else:
            s1[s[i]].append(i)
        if t[i] not in t1.keys():
            t1[t[i]] = [i]
        else:
            t1[t[i]].append(i)
    # print(sorted(s1.values()), sorted(t1.values()))
    if sorted(s1.values()) != sorted(t1.values()):
        return False
    else:
        return True

def containsNearbyDuplicate(n):
    if n <=0:
        return 0
    num = bin(n)
    ret = num[3:]
    ret = ret.strip('0')
    print(num, ret)
    if not ret:
        return True
    return False
    return num[3:]





if __name__ == "__main__":
    # print(trailingZeroes(25))  # 6个=5个5+1个25
    # print('15511210043330985984000000'.count('0'))

    # print(containsNearbyDuplicate(0))
    print(isUgly(14))


