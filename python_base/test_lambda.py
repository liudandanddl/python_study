#!/usr/bin/env python
# coding=utf-8
__author__ = 'ldd'


'''
foo 表示是函数。
foo() 表示执行foo函数。
lamdba主体是一个表达式，而不是一个代码块，函数体比def简单很多。仅仅能在lamdba表达式中封装有限的逻辑进去。
lamdba表达式是起到一个函数速写的作用，允许在代码内嵌入一个函数的定义。

'''


def foo():
    print("foo")


def action(x):
    return lambda y: x+y

if __name__ == "__main__":
    foo()
    print("foo()1: ")
    print("-------------------------------")

    foo = lambda x: x + 1  # 执行下面的lambda表达式，而不再是原来的foo函数，因为foo函数被重新定义了。
    foo(1)
    print("foo()2: ", foo(1))
    func = lambda x, y, z: x+y+z
    print("func(): ", func(1, 2, 3))  # ('func(): ', 6)
    print("-------------------------------")

    a = action(2)
    print("a: ", a)   # a是action函数的返回值， y = 2+y
    print("a(22): ", a(22))   # a(22)即是调用了action返回的lambda表达式


