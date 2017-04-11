#!/usr/bin/env python
# coding=utf-8
from atexit import register
import threading
from time import sleep
import time

__author__ = 'ldd'
'''
python代码的执行是由Python虚拟机(又名解释器主循环)进行控制的。在主循环中同时只能有一个控制线程在执行，就像单核CPU系统中的多进程一样。
内存中可以有许多程序，但是在任意给定时刻只有一个线程会被解释器执行。
对Python虚拟机的访问是由全局解释器(GIL)控制的，这个锁就是用来保证同时只能有一个线程运行的。
由于Python的GIL限制，多线程更适合于I/O密集型应用(I/O释放了GIL，可以允许更多的并发)。
对于计算密集型应用，为了实现更好的并行性，建议使用多进程，以便让CUP的其他内核来执行。
'''
var = ('\n'
       'Python的多线程适合IO密集型，不适合计算密集型应用\n'
       '创建线程常用的3种方法：\n'
       '1.创建Thread的实例，传给它一个函数\n'
       '2.创建Thread的实例，并传给它一个可调用的类的实例\n'
       '3.派生Thread的子类，并创子类的实例\n'
       '当需要一个封建符合面向对象的接口时趋向选择3，否则趋向选择1\n'
       )

loops = [4, 2]


# 函数名最前面的单下划线表示这是一个特殊函数，只能被本模块的代码使用，不能被其他使用本文件作为库或者工具模块的应用导入
def _loop(nloop, nesc):
    print('start loop:', nloop, 'at:', time.time())
    sleep(nesc)
    print('loop', nloop, 'done at:', time.time())


def main1():
    print('1创建Thread的实例，并传给它一个函数')
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=_loop, args=(i, loops[i]))  # args不洗有值，如果所传函数如果没有参数，则args=()一个空的元组
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print('all DONE at:', time.time())


class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.args = args
        self.func = func

    def __call__(self):
        self.func(*self.args)


def main2():
    print('2创建Thread的实例，并传给它一个可调用的类的实例')
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=ThreadFunc(_loop, (i, loops[i]), _loop.__name__))  # 实际上完成了2个实例化，Thread和ThreadFunc
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print('all DONE at:', time.time())


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.args = args
        self.func = func

    def run(self):
        self.func(*self.args)


def main3():
    print('3派生Thread的子类，并创子类的实例')
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = MyThread(_loop, (i, loops[i]), _loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    '''
    对所有线程调用join()不是必须的没因为他们不是守护线程，无论如何主线程都不会再派生线程完成之前退出脚本。
    但是如果没有join()，主线程不会等在这里，会继续往下执行，只是不会退出，会等待所有派生线程完成之后再退出。
    PS：一个新的字线程会继承父进程的守护标记
        主线程将再所有非守护线程退出之后才退出。
    '''
    # for i in nloops:
    #     threads[i].join()
    # print('all DONE at:', time.time())

'''
atexit.register
该函数(使用了装饰器的方式)会在Python解释器中注册一个退出函数，也就是说，它会在脚本退出之前请求调用这个特殊的函数。
如果不是用装饰器，也可以直接使用register(_atexit)
'''
@register
def _atexit():
    print('all DONE at:', time.time())

# register(_atexit)

if __name__ == "__main__":
    main1()
    # main2()
    # main3()