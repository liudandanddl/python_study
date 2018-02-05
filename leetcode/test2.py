#!/usr/bin/env python
# coding=utf-8
from collections import Counter
import re

__author__ = 'ldd'


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    c = Counter(nums)
    print(c)
    return c.most_common(1)[0][0]

if __name__ == "__main__":
    s = "  A man, a plan, a canal: Panama  "
    print(majorityElement([1]))



