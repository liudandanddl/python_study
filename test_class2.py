#!/usr/bin/env python
# coding=utf-8
__author__ = 'ldd'


class Bird(object):
    def __init__(self):  # 构造函数
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("Aaaah")
            self.hungry = False
        else:
            print("No Thanks")


class SongBird(Bird):
    def __init__(self):
        # super方法被用来调用父类的方法，在任何的被重写的方法中都可以使用
        super(SongBird, self).__init__()  # super函数只在新式类中起作用，父类的hungry特性和赋值子类都会拥有
        # Bird.__init__(self)  # 调用未绑定的超类构造方法，效果同super函数，但super函数更好些
        self.sound = 'Squawk'

    def sing(self):
        print(self.sound)


class Rectangle(object):
    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self, size):  # setSize和getSize叫做访问器函数
        self.width, self.height = size

    def getSize(self):
        return self.width, self.height
    # property函数只能新式类用，property函数创建了一个属性
    size = property(getSize, setSize)  # property取代访问器函数


if __name__ == "__main__":
    # sb = SongBird()
    # sb.sing()  # Squawk
    # sb.eat()  # Aaaah 在调用的时候，super函数会查找所以超类(以及超类的超类)，直到找到所需的特性为止(或者引发一个AttributeError异常)
    # sb.eat()  # No Thanks

    r = Rectangle()
    r.width = 10;r.height = 5
    print(r.size)  # (10, 5) 相当于r.getSize()
    r.size = 150, 100  # 相当于r.setSize(150. 100)
    print(r.width)  # 150