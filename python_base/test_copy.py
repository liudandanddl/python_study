#!/usr/bin/env python
# coding=utf-8

__author__ = 'ldd'


if __name__ == "__main__":
    lista = [1, 2]
    # 浅拷贝
    listb = lista[:]
    print(id(lista[0]), id(listb[0]))  # (140412175014024, 140412175014024), 元素的id值是一样的
    print(id(lista), id(listb), lista, listb)  # id值是不一样的，内容一样
    listb[0] = 0
    lista.append(3)
    # a和b的改变不会互相影响
    print("lista=", lista, "id(lista)=", id(lista))  # ('lista=', [1, 2, 3], 'id(lista)=', 4447734168)
    print("listb=", listb, "id(lisb)=", id(listb))  # ('listb=', [0, 2], 'id(lisb)=', 4447733880)
    # 正常copy过来的元素的id值是一样的，更改后地址值变更
    for i in lista:
        print("lista.", i, "=", id(i))  # 140412175014024，140412175014000，140412175013976
    for i in listb:
        print("listb.", i, "=", id(i))  # 140412175014048，140412175014000

    listc = lista  # id和值完全一样
    print(id(listc), id(lista), listc, lista)
    listc[0] = 9
    print(id(listc), id(lista), listc, lista)
    for i in lista:  # 元素的id值也相同，改变互相影响
        print("lista.", i, "=", id(i))  # 140412175014024，140412175014000，140412175013976
    for i in listc:
        print("listc.", i, "=", id(i))