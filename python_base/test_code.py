# -*- coding: utf-8 -*-
# @Date    : 2020-06-22
# @Author  : liudandan

import json


if __name__ == '__main__':
    with open("a.json", 'rb') as f:
        json1 = f.read()
    dit = json.loads(json1)
    value = dit['a']
    print(value)
    name = value.encode('ascii').decode('unicode_escape')  # 文件中的ascii码转中文
    print(name)
    b = '\u5143'
    print(b)
