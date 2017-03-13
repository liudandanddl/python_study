#!/usr/bin/env python
# coding=utf-8
from _socket import AF_INET, SOCK_DGRAM
from socket import socket
from time import ctime

__author__ = 'ldd'

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


# UDP是无链接的，因此先启动客户端还是服务端都可以。不需要监听。
if __name__ == "__main__":
    udpSerSock = socket(AF_INET, SOCK_DGRAM)  # 创建服务器套接字, 用的是IPV4
    udpSerSock.bind(ADDR)  # 套接字与地址绑定
    while True:  # 服务器无限循环
        print("waiting for message......")
        data, addr = udpSerSock.recvfrom(BUFSIZ)  # 接受客户端链接
        print("data: ", data)
        a = ctime().encode('utf-8')
        data = '[%s] %s' % (a, data)
        # 将客户端传过来的数据加上时间戳在传回去
        udpSerSock.sendto(data, addr)  # 被动的等待消息，发回的时候需要指定返回给谁
        print('received from and returned to :', addr)
    udpSerSock.close()

