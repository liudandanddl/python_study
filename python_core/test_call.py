#!/usr/bin/env python
# coding=utf-8
__author__ = 'ldd'

'''
一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call__()
'''


def get_gender(gender):
    print("gender is ", gender)


class Person(object):
    def __init__(self, func, name, gender):
        self.name = name
        self.gender = gender
        self.func = func

    def __call__(self, friend):
        print('person1 name is ', self.name)
        print('2 name is', friend)
        self.func(self.gender)

if __name__ == "__main__":
    f = abs  # 求绝对值函数
    print(f.__name__)  # abs
    # 由于f可以被调用，所以f被称为可调用对象
    print(f(-123))  # 123
    p = Person(get_gender, 'Bob', 'male')
    # ('person1 name is ', 'Bob')
    # ('2 name is', 'Time')
    # ('gender is ', 'male')
    p('Time')  # 这个类直接被调用