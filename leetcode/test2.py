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



if __name__ == "__main__":
    print((10))  # 6个
    # print('15511210043330985984000000'.count('0'))


