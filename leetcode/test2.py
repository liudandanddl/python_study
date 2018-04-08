#!/usr/bin/env python
# coding=utf-8
from collections import Counter

__author__ = 'ldd'


def firstUniqChar(s):
    if not s:
        return -1
    if len(s) == 1:
        return 0
    if s[0] not in s[1:]:
        return 0
    for i in range(1, len(s)-1):
        print(i, s[i], s[i+1:], s[:i])
        if s[i] not in s[i+1:] and s[i] not in s[:i]:
            return i
    if s[-1] not in s[:len(s)-1]:
        return len(s)-1
    return -1







if __name__ == "__main__":
    print(firstUniqChar("aadb"))
