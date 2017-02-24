#!/usr/bin/env python
# coding=utf-8
__author__ = 'ldd'
import ConfigParser  # 解析配置模块


def read_ConfigParser(path):
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    secs = cf.sections()
    print('sections:', secs)  # sections: ['sec_a', 'sec_b']
    opts = cf.options("sec_a")
    print('options:', opts)  # sections名字为sec_a这个的所有options: ['a_key1', 'a_key2']
    kvs = cf.items("sec_a")
    print('sec_a:', kvs)  # sec_a: [('a_key1', '20'), ('a_key2', '10')]

    str_val = cf.get("sec_a", "a_key1")
    int_val = cf.getint("sec_a", "a_key2")

    print("value for sec_a's a_key1:", str_val)
    print("value for sec_a's a_key2:", int_val)


# 将path下的文件重新写到test.conf里面，并添加了一些元素
def write_ConfigParser(path):
    cf = ConfigParser.ConfigParser()
    cf.read(path)
    # update value
    cf.set("sec_b", "b_key3", "new-$r")
    # set a new value
    cf.set("sec_b", "b_newkey", "new-value")
    # create a new section
    cf.add_section('a_new_section')
    cf.set('a_new_section', 'new_key', 'new_value')

    # write back to configure file
    cf.write(open("test.conf", "w"))

if __name__ == "__main__":
    path = "test_onfigParser.conf"
    read_ConfigParser(path)
    write_ConfigParser(path)