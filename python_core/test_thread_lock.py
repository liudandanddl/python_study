#!/usr/bin/env python
# coding=utf-8
from atexit import register
from random import randrange
from threading import Lock, currentThread, Thread
from time import ctime, sleep

__author__ = 'ldd'

var = ('\n'
       '线程同步，使用下面3种同步原语：\n'
       '1.锁 acquire()和release()操作\n'
       '2.上下文管理，with语句\n'
       '3.信号量:比锁更强大的同步原语。它是一个计数器，他们从固定数量的有限资源开始，当资源消耗时递减，当资源释放时递增。'
       '  Threading模块包括两种信号量：Semaphore和BoundedSemaphore。BoundedSemaphore的一个额外功能是这个计数器的值永远不会超过它的初始值，'
       '  换句话说，它可以防范其中信号量释放次数多于获得次数的异常用例发生此种情况的时候抛异常'
       '  Python使用和锁的函数一样的名字：acquire和release'
       '  acquire：对应P()，消耗资源使计数器递减'
       '  release：对应V()，资源释放，使计数器递增。\n'
       )


class CleanOutputSet(set):  # 实现set的str方法，将默认输出改变为将其所有元素按照逗号分隔的字符串
    def __str__(self):
        return ', '.join(x for x in self)

# 3个全局变量
lock = Lock()  # 锁
loops = (randrange(2, 5) for x in xrange(randrange(3, 7)))  # 随机数量的线程(3-6个线程)，每个线程睡眠时间2-4秒
remaining = CleanOutputSet()


# 如果不用锁，可能输出部分混乱(因为多个线程可能并行执行I/O)
# 两个线程修改同一个变量(剩余线程集合remaining)名。
def loop(nesc):
    myname = currentThread().name  # 返回当前Thread的对象名字
    lock.acquire()  # 获取锁
    remaining.add(myname)
    print('[%s] Started %s' % (ctime(), myname))
    lock.release()  # 释放锁
    sleep(nesc)  # 执行睡眠操作
    lock.acquire()  # 重新获得锁
    remaining.remove(myname)
    print(ctime(), ' Completed ', myname, str(nesc))  # 进行最终输出
    print('remaining: %s' % (remaining or 'NONE'))
    lock.release()  # 释放锁


# 使用上下文管理
# 使用with语句，可以不再调用acquire()和release()方法，Python版本在2.5以上
# 使用with语句，此时每个对象的上下文管理器负责在进入该套件之前调用acquire并在完成执行之后调用release
def loop1(nesc):
    myname = currentThread().name  # 返回当前Thread的对象名字
    with lock:
        remaining.add(myname)
        print('[%s] Started %s' % (ctime(), myname))
    sleep(nesc)  # 执行睡眠操作
    with lock:
        remaining.remove(myname)
        print(ctime(), ' Completed ', myname, str(nesc))  # 进行最终输出
        print('remaining: %s' % (remaining or 'NONE'))


def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()


def _main1():
    for pause in loops:
        Thread(target=loop1, args=(pause,)).start()


@register
def _atexit():
    print('all DONE at:', ctime())


if __name__ == '__main__':
    print('all START at:', ctime())
    # _main()
    _main1()