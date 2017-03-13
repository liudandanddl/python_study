#!/usr/bin/env python
# coding=utf-8
from _socket import AF_INET, SOCK_STREAM
from socket import socket
from time import ctime

__author__ = 'ldd'

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


if __name__ == "__main__":
    tcpSerSock = socket(AF_INET, SOCK_STREAM)  # 创建服务器套接字, 用的是IPV4
    tcpSerSock.bind(ADDR)  # 套接字与地址绑定
    tcpSerSock.listen(5)
    while True:  # 服务器无限循环
        print("waiting for connection......")
        tcpCliSock, addr = tcpSerSock.accept()  # 接受客户端链接
        print("...connected from: ", addr)

        while True:  # 通信循环
            data = tcpCliSock.recv(BUFSIZ)  # 接受客户端传过来的数据
            if not data:
                break
            # 将客户端传过来的数据前面加上时间戳在传回去
            print("data: ", data)
            a = ctime().encode('utf-8')
            print(a)
            data = '[%s] %s' % (a, data)
            tcpCliSock.send(data)
        tcpCliSock.close()  # 关闭客户端套接字
    tcpSerSock.close()  # 关闭服务器套接字，理论上永远不会执行本行

