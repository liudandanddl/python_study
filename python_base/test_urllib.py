#!/usr/bin/env python
# coding=utf-8
from urllib import urlopen

__author__ = 'ldd'


if __name__ == "__main__":
    # webpage是一个连接到该网址的网页的类文件对象，支持close，read，readline, readlines等方法，当然也支持迭代
    webpage = urlopen("http://www.baidu.com")
    # for preline in webpage:
    #     print(preline)
    lines = webpage.readlines()
    print(lines.__len__())
    print(lines[0])
