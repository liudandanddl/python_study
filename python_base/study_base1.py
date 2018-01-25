#!/usr/bin/env python
# coding=utf-8
__author__ = 'ldd'

'''
Python的垃圾回收机制：Python使用引用计数来追踪对象，并释放不再引用的对象。
'''


def square(x):
    '函数的文档字符串，使用函数名.__doc__可以访问,函数的注释应该使用文档字符串的形势，必须在函数的第一行'
    return x*x


if __name__ == "__main__":
    # print(square.__doc__)
    # print(help(square))

    # s = 'as'
    # if s.endswith('a', 0, 1):
    #     print("1111")

    # s = [1, 2, 3]
    # y = s  # y和s是同一对象， is判断是否是同意对象
    # s[1] = 1
    # print(y, s is y)  # ([1, 1, 3], True)
    # s1 = [1, 2, 3]
    # y1 = s1[:]  # 利用切片赋值，y和s是不同对象，浅拷贝
    # s1[1] = 1
    # print(y1, s1 is y1)  # ([1, 2, 3], False)

    # dict1 = {'k1':'v1', 'k2':'v2'}
    # for k, v in dict1.items():  # items将字典的key和value以元组形式展示
    #     print(k + v)
    # print(dict1.items())
    # list1 = [1,2,3]
    # for d, l in zip(dict1.items(), list1):  # 序列的并行迭代，处理不等长的序列的时候最短的用完就会停止
    #     print(d, l)

    # list2 = [3,4,2,6,1,9]
    # l_s = sorted(list2)  # 返回列表
    # l_r = reversed(list2)  # 返回可迭代对象
    # print(l_s, type(l_s))
    # print(list(l_r), type(l_r))

    i = 3
    def change(a):
        # 不能再内部改变全局变量的值
        i + a
        print(i+a)
    print(i)
    change(2)