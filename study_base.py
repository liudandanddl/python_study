#!/usr/bin/env python
# coding=utf-8
__author__ = 'ldd'


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
    # y1 = s1[:]  # 利用切片赋值，y和s是不同对象
    # s1[1] = 1
    # print(y1, s1 is y1)  # ([1, 2, 3], False)

    dict1 = {'k1':'v1', 'k2':'v2'}
    for k, v in dict1.items():  # items将字典的key和value以元组形式展示
        print(k + v)
    print(dict1.items())
    list1 = [1,2,3]
    for d, l in zip(dict1.items(), list1):  # 序列的并行迭代
        print(d, l)