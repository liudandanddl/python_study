#!/usr/bin/env python
# coding=utf-8

__author__ = 'ldd'


if __name__ == "__main__":
    lista = [1, 2]
    # 浅拷贝
    listb = lista[:]
    print(id(lista), id(listb))
    listb[0] = 0
    lista.append(3)
    print("lista=", lista, "id(lista)=", id(lista))
    print("listb=", listb, "id(lisb)=", id(listb))
    for i in lista:
        print("lista.", i, "=", id(i))
    for i in listb:
        print("listb.", i, "=", id(i))