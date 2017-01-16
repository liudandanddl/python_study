#!/usr/bin/env python
# coding=utf-8
__author__ = 'ldd'

# Python 装饰器简介


def check_login():
    # 验证1， 验证2
    pass


def f1():
    check_login()
    print("f1")


def f2():
    check_login()
    print("f2")
'''
我们正常如上述修改代码逻辑。修改成装饰器的模式，该段代码如下所述：
'''


def check_lo(func):
    def inner():
        # 验证1， 验证2
        return func()
    return inner()


@check_lo
def f1():
    print("f1")


@check_lo
def f2():
    print("f2")
'''
当写完这段代码后(函数未被执行)，Python解释器就会从上到下解释代码，步骤如下：
1.def check_lo(func): ==>将check_lo函数加载到内存
2.@check_lo 从表面上看解释器仅仅会解释这两句代码，因为函数在没有被调用之前其内部代码不会被执行。
  @check_lo内部会执行以下操作：
  （1）执行check_lo函数，并将@check_lo下面的函数作为check_lo函数的蚕食，即：@check_lo等价于check_lo(f1)，所以，内部就会执行：
       def inner:
       # 验证1， 验证2
       return f1()  func是参数，此时func等于f1
       return inner()  返回的inner，inner代表的是函数，非执行函数
'''
