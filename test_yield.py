#!/usr/bin/env python
# coding=utf-8
__author__ = 'ldd'

'''
yield 的功能类似于return，但是不同之处在于它返回的是生成器。生成器是一个包含yield的函数。
当它被调用的时候，在函数体中的代码不会被执行，而会返回一个迭代器。
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


def flatten(netsted):
    '展开一个序列'
    try:
        # 将传入的对象和一个字符串拼接，看看会不会出现TypeError，这是检查一个对象是不是类似于字符串的最简单、最快速的方法
        try:
            netsted + ''
        except TypeError:
            pass  # 非字符串，什么都不做，继续下面的for循环
        else:
            raise TypeError  # 如果是字符串，则不会引发TypeError，所以自己排除一个TypeError，会被下面的except代码捕获
        for sublist in netsted:
            for element in flatten(sublist):  # 当sublist不可迭代时(比如数字)就会引发TypeError异常。
                yield element
    except TypeError:
        yield netsted
'''
# flatten函数不用yield生成器，用普通函数重写
def flatten(netsted):
    '展开一个序列'
    result = []
    try:
        try:
            netsted + ''
        except TypeError:
            pass  # 非字符串，什么都不做，继续下面的for循环
        else:
            raise TypeError  # 如果是字符串，则不会引发TypeError，所以自己排除一个TypeError，会被下面的except代码捕获
        for sublist in netsted:
            for element in flatten(sublist):  # 当sublist不可迭代时(比如数字)就会引发TypeError异常。
                result.append(element)
    except TypeError:
        result.append(netsted)
    return result
'''

if __name__ == "__main__":
    f = func()
    print(list(f))  # 使用list方法显示地将迭代器转化为列表
    # StopIteration 如果next方法被调用，但迭代器没有值可以返回，就会引发StopIteration异常
    for i in range(0, 5, 1):
        print(f.next())  # yield返回的是一个可迭代对象，使用迭代器迭代(next方法)

    print("---------------------------------")
    f1 = func1()
    print("f1.next(): ", f1.next())
    print("f1.next()2: ", f1.next())
    print("f1.send(5)", f1.send(5))  # n 赋值为5. yield方法返回一个值，也就是外部通过send方法发送的值，如果next方法被使用，那么yield方法返回None
    print(f1.next())

    netsted = [[1, 2], [3, 4, 5], [6, [7, [8, 9], 10]], ['zoo']]
    print(list(flatten(netsted)))

