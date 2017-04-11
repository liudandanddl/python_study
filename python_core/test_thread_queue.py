#!/usr/bin/env python
# coding=utf-8
from Queue import Queue
from random import randint
from time import sleep
from python_core.test_thread import MyThread

__author__ = 'ldd'


def writeQ(queue):
    print('producing object for Q...')
    queue.put('test', 1)  # 将一个对象(字符串test)放入队列中， 每次只会产生一个对象
    print('xize now', queue.qsize())  # qsize返回队列大小，由于返回时队列大小可能被其他线程修改，所以该值为近似值


def readQ(queue):
    val = queue.get(1)  # 将一个对象从队列中读取，每次只会读取一个对象
    print('consumed object from Q... size now', queue.qsize(), 'val=', val)


def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1, 3))


def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2, 5))


funcs = [writer, reader]
nfuncs = range(len(funcs))


def _main():
    nloops = randint(2, 5)
    q = Queue(32)  # 创建一个先入先出队列，最大值32，在队列没有空间的时候阻塞。如果没有指定最大值，为无线队列
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print('all DONE')


if __name__ == '__main__':
    _main()