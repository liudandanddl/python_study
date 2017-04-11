#!/usr/bin/env python
# coding=utf-8
from atexit import register
from random import randrange
from threading import Lock, BoundedSemaphore, Thread
from time import sleep, ctime

__author__ = 'ldd'
var = ('\n'
       '线程同步，信号量:比锁更强大的同步原语。它是一个计数器，他们从固定数量的有限资源开始，当资源消耗时递减，当资源释放时递增。'
       '  Threading模块包括两种信号量：Semaphore和BoundedSemaphore。BoundedSemaphore的一个额外功能是这个计数器的值永远不会超过它的初始值，'
       '  换句话说，它可以防范其中信号量释放次数多于获得次数的异常用例发生此种情况的时候抛异常'
       '  Python使用和锁的函数一样的名字：acquire和release'
       '  acquire：对应P()，消耗资源使计数器递减'
       '  release：对应V()，资源释放，使计数器递增。\n'
       )
'''
模拟一个简化的糖果机，该机器只有5个可用的槽来保持库存(糖果)。如果所有的槽都满了，糖果就不能加进机器，如果所有槽空了，顾客就不能买到糖果。
使用信号量来跟踪这些有限的资源(糖果槽)
'''

lock = Lock()  # 全局变量，锁
MAX = 5  # 库存商品最大值的常量
candytray = BoundedSemaphore(MAX)  # 跟踪有限资源的信号量


# 向库存中添加糖果
def refill():
    lock.acquire()
    print 'Refilling candy...',   # 打印不换行
    try:
        candytray.release()  # 计数器递增
    except ValueError:
        print('full , skipping')  # 添加糖果唱过库存的时候，给以警告
    else:
        print('OK')
    lock.release()


# 消费者购买糖果
def buy():
    lock.acquire()
    print 'Buying candy...',
    if candytray.acquire(False):  # 检查是否左右资源都已耗尽。通过传入非阻塞的标志FALSE，让调用不在阻塞，而在应当阻塞的时候返回一个FALSE，指明没有更多资源。
        print('OK')
    else:
        print('empty, skipping')
    lock.release()


def producer(loops):
    for i in xrange(loops):
        refill()
        sleep(randrange(3))


def consumer(loops):
    for i in xrange(loops):
        buy()
        sleep(randrange(3))


def _main():
    print('starting at:', ctime())
    nloops = randrange(2, 6)
    print('THE CANDY MACHINE (full with %d bars)!') % MAX
    Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2),)).start()  # 购买糖果的个数2活3，4，5，6，7
    Thread(target=producer, args=(nloops,)).start()  # 放入糖果的个数2或3，4，5，


@register
def _atexit():
    print('all DONE at:', ctime())


if __name__ == "__main__":
    _main()






