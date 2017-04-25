#!/usr/bin/env python
# coding=utf-8
__author__ = 'ldd'

global num
num = 1
l = [1]
def ptest1():
    print('test1=',num, id(num), l, id(l), id(l[0]))