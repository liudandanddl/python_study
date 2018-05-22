# coding=utf-8
class X(object):
    def f(self):
        print 'x'

class A(X):
    def f(self):
        test = 11
        print 'a'
        print(test)

    def extral(self):
            print 'extral a'

class B(X):
    def f(self):
        print 'b'

    def extral(self):
            print 'extral b'

class C(A, B, X):
    def f(self):  # 此方法覆盖了父类中的f方法，父类中的f方法不在生效
        print('c')
        test = 12
        print(test)

# print C.mro()  # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.X'>, <type 'object'>]
# 多类继承使用广度优先搜索，MRO（Method Resolution Order）：方法解析顺序

c = C()
c.f()  # c 12
c.extral() # extral a

class D(A, B, X):
    def f(self):
        super(D, self).f() # super两个作用：继承父类的所有方法和属性，不会被重写或者覆盖；父类类名修改之后，不需要在所有子类中进行类名修改
        #  等价代码是A.f(self)
        print 'd'
        test = 12
        print(test)
d = D()
d.f()  # a 11 d 12
d.extral() # extral a