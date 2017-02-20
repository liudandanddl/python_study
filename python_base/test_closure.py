#!/usr/bin/env python
# coding=utf-8
__author__ = 'ldd'

# 闭包:类似test2函数存储子封闭作用域内的行为叫做闭包


def test1(a1):
    def test2(a2):
        print('a1:', a1, 'a2:', a2)
        return a1*a2
    return test2

if __name__ == "__main__":
    d = test1(2)
    print(d)  # <function test2 at 0x1073cc0c8>
    print(d(5))  # ('a1:', 2, 'a2:', 5)