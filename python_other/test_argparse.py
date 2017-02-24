#!/usr/bin/env python
# coding=utf-8
import argparse   # 命令行选项及参数解析，Python2.7以后版本支持

__author__ = 'ldd'

'''
返回值类型<class 'argparse.Namespace'>
dest就是类的属性，default是属性默认值，actions是存储参数默认是store，前面的-X是区分X随便写
'''
def parse_args():
    # 建立解析器
    parser = argparse.ArgumentParser(description='Process some integers.')
    # 参数根据add_argument()的action选项触发不同action。支持的action有存储参数（单个，或作为列表的一部分）;
    # 存储常量的值（对布尔开关true/false有特殊处理）。默认动作是存储参数值。支持type(指定存储类型)和dest(指定存储变量)等参数。
    parser.add_argument('-L', action='store', dest='simple_value', help='Storea simple value')
    parser.add_argument('-c', action='store_const', dest='constant_value', const='value-to-store', help='Store a constant value')
    parser.add_argument('-t', action='store_true',default=False,dest='boolean_switch',help='Set a switch to true')
    parser.add_argument('-f', action='store_false', default=False,dest='boolean_switch', help='Set a switch to false')
    parser.add_argument('-a', action='append', dest='collection',default=[], help='Add repeated values to a list')
    parser.add_argument('-A', action='append_const', dest='const_collection',const='value-1-to-append',default=[],help='Add different values to list')
    parser.add_argument('-B', action='append_const',dest='const_collection', const='value-2-to-append',help='Add different values to list')
    parser.add_argument('--version', action='version',version='%(prog)s 1.0')
    # 使用函数parse_args()进行参数解析，这个函数的输入默认是sys.argv[1:]，也可以使用其他字符串列表。
    args = parser.parse_args()
    return args

if '__main__' == __name__:
    args = parse_args()
    print(args)   # Namespace(conf='conf/flow_replay.cfg', product='gs')
    print(type(args))  # <class 'argparse.Namespace'>
    print 'simple_value    = %r' % args.simple_value
    print 'constant_value  = %r' % args.constant_value
    print 'boolean_switch  = %r' % args.boolean_switch
    print 'collection      = %r' % args.collection
    print 'const_collection = %r' % args.const_collection


'''
在命令行下执行如下语句
python test_argparse.py --version
python test_argparse.py --s value1
python test_argparse.py -c
python test_argparse.py -t
python test_argparse.py -f
python test_argparse.py -a on -a tw
python test_argparse.py -B -A
python test_argparse.py -s val1 -c -t -a on -a tw -B -A
'''

