#!/usr/bin/env python
# coding=utf-8
import timeit

__author__ = 'ldd'
'''
如果两个代码完成相同的工作，使用timeit可以知道哪一种效率更高
'''

if __name__ == "__main__":
    # str = 's="Subject: XXX"'
    # t1 = timeit.Timer('s[:8] == "Subject:"', str)
    # print(t1.timeit())  # 0.099426984787
    #
    # t2 = timeit.Timer('s.startswith("Subject:")', str)
    # print(t2.timeit())  # 0.213320016861

    t1 = timeit.Timer('l1[1::2] = len(l1[1::2])*[1]', 'l1 = [0]*10')
    print(t1.timeit())
    print('~~~~~~~~~~~~~')
    t2 = timeit.Timer('for i in range(1, len(l2), 2):l2[i] = 1', 'l2 = [0]*10')
    print(t2.timeit())

    '''
    数据量100的时候： t1 = 1.47810101509    t2 = 3.01431393623
    数据量1000的时候：t1 = 8.62256288528    t2 = 27.588889122
    '''