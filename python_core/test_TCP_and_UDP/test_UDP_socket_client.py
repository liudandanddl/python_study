#!/usr/bin/env python
# coding=utf-8
from _socket import AF_INET, SOCK_DGRAM
from socket import socket

__author__ = 'ldd'


HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


if __name__ == "__main__":
    udpCliSock = socket(AF_INET, SOCK_DGRAM)  # 创建客户端套接字, 用的是IPV4
    while True:
        data = raw_input('>')
        if not data:
            break
        udpCliSock.sendto(data, ADDR)
        data = udpCliSock.recvfrom(BUFSIZ)
        if not data:
            break
        print(data)  # 返回的数据data是个元组
        print(data[0].decode('utf-8'))
    udpCliSock.close()