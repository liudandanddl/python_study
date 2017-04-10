#!/usr/bin/env python
# coding=utf-8
import timeit

__author__ = 'ldd'
'''
如果两个代码完成相同的工作，使用timeit可以知道哪一种效率更高
'''

if __name__ == "__main__":
    str = 's="Subject: XXX"'
    t1 = timeit.Timer('s[:8] == "Subject:"', str)
    print(t1.timeit())  # 0.099426984787

    t2 = timeit.Timer('s.startswith("Subject:")', str)
    print(t2.timeit())  # 0.213320016861