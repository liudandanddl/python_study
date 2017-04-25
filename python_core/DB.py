#!/usr/bin/env python
# coding=utf-8
__author__ = 'ldd'
'''
Python数据库应用结构：
（1）应用(嵌入式)                                                        -- RDBMS客户端库 -- 关系数据库(RDBMS)
（2）Python应用(嵌入SQL)                    -- Python数据库适配器(DB-API) -- RDBMS客户端库 -- 关系数据库(RDBMS)
（3）Python应用(少量或没有SQL) -- Python ORM -- Python数据库适配器(DB-API) -- RDBMS客户端库 -- 关系数据库(RDBMS)

Python适配器是一个Python模块，使用它可以与关系数据的客户端库(通常是C语言编写的)接口相连。
Python的DB-API：connect()函数，Connection对象，Cursor对象，数据类型对象
（2）这种无Python ORM的情况，都是使用DB-API显示的写入SQL语句。
（3）这种直接操作ORM，几乎无显示的SQL语句。

ORM(对象关系映射)：考虑对象，而不是SQL。将纯SQL语句进行了抽象化处理，将其实现为Python中的对象。比较知名的两款ORM：SQLAlchemy和SQLObject。
SQLAlchemy：的接口更加接近于SQL语句。两种使用：
（1）自定义数据子类基础Base类(declarative_base()),增删改查使用session对象。
（2）创建Table对象而不是声明Base对象，无session对象，增删改查使用Table对象操作。
SQLObject：更简单、快速、Python化。不支持Python3.x版本
自定义数据子类基础SQLObject类。无session对象，直接操作自定义数据子类进行增删改查操作。

MongoDB：文档存储非关系数据库，文档存储系统使用C++编写的。
一般情况下其数据会另存为JSON对象，并且允许诸如字符串、数值、列表甚至嵌套等数据类型。
MongoDB的集合(JSON对象)对应的是关系数据库的表。JSON中的key对应数据库表的列。
PyMongo：MongoDB的Python驱动程序之一。

'''