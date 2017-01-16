#!/usr/bin/env python
# coding=utf-8
__author__ = 'ldd'

'''
yield 的功能类似于return，但是不同之处在于它返回的是生成器。
生成器不会一次返回所有结果，而是每次遇到yield关键字后返回相应结果，并保留函数当前的运行状态，等待下一次的调用。
由于生成器也是一个迭代器，支持next方法来获取下一个值。
除了next函数，生成器还支持send函数，该函数可以向生成器传递参数。
最常见的应用是生产无限序列。
'''


def func():
    for i in xrange(5):
        yield i


def func1():
    n = 0
    while 1:
        n = yield n  # 可以通过send函数向n赋值

if __name__ == "__main__":
    f = func()
    for i in range(0, 5, 1):
        print(f.next())

    print("---------------------------------")
    f1 = func1()
    print("f1.next(): ", f1.next())
    print("f1.next()2: ", f1.next())
    print("f1.send(5)", f1.send(5))  # n 赋值为5

