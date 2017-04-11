#!/usr/bin/env python
# coding=utf-8
__author__ = 'ldd'


class setOW(set):
    def __str__(self):
        return ', '.join(x for x in self)

if __name__ == "__main__":
    a = set()
    a.add('1')
    a.add('2')
    print(a)  # set(['1', '2'])

    b = setOW()
    b.add('1')
    b.add('2')
    print(b)  # 1, 2