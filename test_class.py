#!/usr/bin/env python
# coding=utf-8
__author__ = 'ldd'

__metaclass__ = type  # python3.0以上新式类的语法，在模块或者脚本开始的地方放置该赋值语句。也可以继承新式类(比如object)


class Demol:

    members = 0
    self_mem = 0

    def members_count(self):
        # 下面二者类似于函数内的局部和全局变量
        Demol.members += 1  # 类作用域内的变量被所有实例访问
        self.self_mem += 1  # 被一个实例访问

if __name__ == "__main__":
    d1 = Demol()
    d1.members_count()
    print('Demol.members', Demol.members, 'Demol.self_mem', Demol.self_mem)
    print('d1.members', d1.members, 'd1.self_mem', d1.self_mem)
    d2 = Demol()
    d2.members_count()
    print('Demol.members', Demol.members, 'Demol.self_mem', Demol.self_mem)
    print(d1.members, d2.members, d1.self_mem, d2.self_mem)

    print(hasattr(d1, 'members'))  # 检查方法或属性是否存在，返回值布尔值
    print(getattr(d1, 'members'))  # 相当于d1.members 对应的是setattr()
    print(hasattr(getattr(d1, 'members_count'), '__call__'))  # 检查方法或属性是否可调用，返回值布尔值 True
    print(hasattr(getattr(d1, 'self_mem'), '__call__'))  # 检查方法或属性是否可调用，返回值布尔值 False
    print(d1.__dict__)  # 查看对象内所有存储的值
    print(Demol.__dict__)  # 查看对象内所有存储的值